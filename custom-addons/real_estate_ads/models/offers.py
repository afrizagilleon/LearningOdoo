from odoo import fields, models, api, _
from datetime import timedelta
from odoo.exceptions import ValidationError


# class AbstractOffer(models.AbstractModel):
#     _name = "abstract.model.offer"
#     _description = "Abstract Offer"
#
#     partner_email = fields.Char(string="Email")
#     partner_phone = fields.Char(string="Phone")

class TransientOffer(models.TransientModel):
    _name = 'transient.model.offer'
    _description = 'Transient Offer'

    # _transient_max_count = 0
    #  it will destroy a value if the max reached, zero if unlimited

    # _transient_max_hours = 0
    # it will destroy any value that reach max hour stay in database

    # @api.autovacuum
    # def _transient_offer(self):
    # It will be called when the new record created


class Offer(models.Model):
    _name = "estate.property.offer"
    # _inherit = ['abstract.model.offer']
    _description = "Offers of the property"

    name = fields.Char(string="Description", compute="_compute_name")
    price = fields.Float(string="Price")
    status = fields.Selection(
        [('accepted', 'Accepted'), ('rejected', 'Rejected')],
        string="Status")

    validity = fields.Integer(string="Validity")
    deadline = fields.Date(
        string="Deadline",
        default=fields.Date.today() + timedelta(days=7),
        compute="_compute_deadline", inverse="_set_deadline", )
    creation_date = fields.Date(string="Creation Date",
                                readonly=True, default=fields.Datetime.now)

    # Relations
    partner_id = fields.Many2one('res.partner', string="Partner", required=True)
    property_id = fields.Many2one('estate.property', string="Property")

    @api.depends('validity')
    def _compute_deadline(self):
        for rec in self:
            rec.deadline = rec.creation_date + timedelta(days=rec.validity)

    @api.onchange('creation_date', 'deadline')
    def _onchange_deadline(self):
        for rec in self:
            rec.validity = (rec.deadline - rec.creation_date).days

            if rec.validity <= 0:
                if not rec.partner_id:
                    raise ValidationError(f'Please select the Partner')

                raise ValidationError(_(f'{rec.partner_id.name}\'s deadline must be greater than creation date'))

    @api.depends('creation_date')
    def _set_deadline(self):
        for rec in self:
            rec.validity = (rec.deadline - rec.creation_date).days

    @api.depends('property_id', 'partner_id')
    def _compute_name(self):
        for rec in self:
            if rec.partner_id and rec.property_id:
                rec.name = f"{rec.property_id.name} - {rec.partner_id.name}"
            else:
                rec.name = False

    def action_accept_offer(self):
        if self.property_id:
            self._validate_accept_offer()
            self.property_id.write({
                'selling_price': self.price,
                'state': 'accepted',
            })
            self.property_id.selling_price = self.price
        self.status = 'accepted'

    def _validate_accept_offer(self):
        offer_ids = self.env['estate.property.offer'].search([
            ('property_id', '=', self.property_id.id),
            ('status', '=', 'accepted'),
        ])
        if offer_ids:
            raise ValidationError(_("You have an accepted offer already"))

    def action_decline_offer(self):
        self.status = 'rejected'
        offers_count = self.property_id.offer_count
        is_all_offers_declined = self.property_id.offer_ids.mapped('status') == ['rejected'] * offers_count
        if is_all_offers_declined:
            self.property_id.write({
                'selling_price': self.price,
                'state': 'received',
            })
            self.property_id.selling_price = 0

    # ORM Command
    # def write(self, vals):
    #     x = self.env['res.partner'].search([
    #         ('is_company', '=', True),
    #     ]).mapped('name')
    #     print(x)
    #     return super(Offer, self).write(vals)
