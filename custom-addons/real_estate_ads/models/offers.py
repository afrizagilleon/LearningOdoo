from odoo import fields, models


class Offer(models.Model):
    _name = "estate.property.offer"
    _description = "Offers of the property"

    price = fields.Float(string="Price")
    status = fields.Selection(
        [('accepted', 'Accepted'), ('rejected', 'Rejected')],
        string="Status")

    validity = fields.Integer(string="Validity")
    deadline = fields.Datetime(string="Deadline")

    # Relations
    partner_id = fields.Many2one('res.partner', string="Partner")
    property_id = fields.Many2one('estate.property', string="Property")
