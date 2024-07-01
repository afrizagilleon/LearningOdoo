from odoo import fields, models, api
from datetime import timedelta


class Offer(models.Model):
    _name = "estate.property.offer"
    _description = "Offers of the property"

    price = fields.Float(string="Price")
    status = fields.Selection(
        [('accepted', 'Accepted'), ('rejected', 'Rejected')],
        string="Status")

    validity = fields.Integer(string="Validity")
    deadline = fields.Date(
        string="Deadline",
        compute="_compute_deadline", inverse=True)
    creation_date = fields.Date(string="Creation Date", default=fields.Datetime.now)

    # Relations
    partner_id = fields.Many2one('res.partner', string="Partner")
    property_id = fields.Many2one('estate.property', string="Property")

    @api.depends('validity', 'creation_date')
    def _compute_deadline(self):
        for rec in self:
            rec.deadline = rec.creation_date + timedelta(days=rec.validity)

    @api.onchange('creation_date', 'deadline')
    def _onchange_deadline(self):
        for rec in self:
            rec.validity = (rec.deadline - rec.creation_date).days
