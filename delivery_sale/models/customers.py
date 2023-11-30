from odoo import models, fields


class DeliverySaleCustomers(models.Model):
    _name = "delivery.sale.customers"
    _inherit = "mail.thread"
    _description = "Envio a Clientes"

    document = fields.Char("Documento de identidad", required=True, size=8, tracking=True)
    name = fields.Char("Apellidos y Nombres", required=True, size=100, tracking=True)
    phone = fields.Char("Celular", size=9, tracking=True)
    address_ids = fields.One2many("delivery.sale.address", "customers_id", "Direcciones")


class DeliverySaleAddress(models.Model):
    _name = "delivery.sale.address"
    _description = "Dirección"

    customers_id = fields.Many2one("delivery.sale.customers", "Cliente")
    name = fields.Char("Lugar", required=True)
    address = fields.Char("Dirección", required=True)

    def name_get(self):
        result = []
        for rec in self:
            name = '{} ({})'.format(rec.name, rec.address)
            result.append((rec.id, name))
        return result
