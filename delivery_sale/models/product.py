from odoo import models, fields


class DeliverySaleProduct(models.Model):
    _name = "delivery.sale.product"
    _description = "Producto"

    name = fields.Char("Nombre del producto", required=True, size=100)
    stock = fields.Integer("Stock")
    price = fields.Float("Precio")
    discount = fields.Float("Descuento %")


class AccountMove(models.Model):
    _inherit = 'account.move'

    demo = fields.Char("Whatapp")


class ResPartner(models.Model):
    _inherit = 'res.partner'

    demo2 = fields.Char("Whatapp")

