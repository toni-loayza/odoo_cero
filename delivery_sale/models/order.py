from odoo import models, fields, api
from ..services.utils import OPTIONS_STATE


class DeliverySaleOrder(models.Model):
    _name = "delivery.sale.order"
    _inherit = "mail.thread"
    _rec_name = "customers_id"
    _description = "Pedido"

    date = fields.Date("Fecha de pedido", default=lambda self: fields.Date.context_today(self), required=True, tracking=True)
    customers_id = fields.Many2one("delivery.sale.customers", "Cliente", required=True, tracking=True)
    address_id = fields.Many2one("delivery.sale.address", "Dirección", required=True, tracking=True)
    state = fields.Selection(OPTIONS_STATE, string="Estado", default='registro', tracking=True)
    line_ids = fields.One2many("delivery.sale.order.line", "order_id", "Detalle de pedido", tracking=True)

    @api.onchange('customers_id')
    def onchange_customers(self):
        self.address_id = False
        if len(self.customers_id.address_ids) == 1:
            self.address_id = self.customers_id.address_ids

    def action_setup(self):
        # self.write({'state': 'registro'})
        self.write({'state': 'preparando'})
        for rec in self.line_ids:
            rec.product_id.stock -= rec.quantity

    def action_finalize(self):
        self.write({'state': 'finalizado'})


class DeliverySaleOrderLine(models.Model):
    _name = 'delivery.sale.order.line'
    _description = "Detalle de pedido"

    order_id = fields.Many2one("delivery.sale.order", "Pedido", required=True)
    product_id = fields.Many2one("delivery.sale.product", "Producto", required=True)
    quantity = fields.Integer("Cantidad", default=1, required=True)
    price_unit = fields.Float(related="product_id.price")
    discount = fields.Float(related="product_id.discount")
    subtotal = fields.Float("Subtotal", compute="compute_subtotal")

    @api.depends('product_id', 'quantity')
    def compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.quantity * rec.price_unit * (1 - rec.product_id.discount / 100)
