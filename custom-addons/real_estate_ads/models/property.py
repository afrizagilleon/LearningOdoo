from odoo import fields, models, api


class Property(models.Model):
    _name = 'estate.property'  # the name Model
    _description = 'Property description'
    _inherit = [
        'mail.thread',
        'mail.activity.mixin',
        # 'utm.mixin',
        'website.published.mixin',
        'website.seo.metadata',
    ]

    name = fields.Char(string='Name', required=True)
    state = fields.Selection([
        ('new', 'New'),
        ('received', 'Offer Received'),
        ('accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('cancel', 'Canceled'),
    ], default='new', string='Status', required=True, group_expand='_expand_estate')
    type_id = fields.Many2one('estate.property.type', string='Type')
    tags_id = fields.Many2many('estate.property.tags', string='Tags')
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Datetime(string='Available From')
    expected_price = fields.Float(string='Expected Price', tracking=True)
    selling_price = fields.Float(string='Selling Price', readonly=True)
    best_offer_price = fields.Float(string='Best Offer Price', compute='_compute_best_offer')
    bedrooms = fields.Integer(string='Bedrooms')
    living_area = fields.Integer(string='Living Area(sqm)')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage', default=False)
    garden = fields.Boolean(string='Garden', default=False)
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Selection([
        ('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')
    ], string='Garden Orientation', default='north')

    total_area = fields.Integer(string='Total Area', compute='_compute_total_area')

    # Relations
    offer_ids = fields.One2many('estate.property.offer',
                                'property_id',
                                string='Offers')
    sales_id = fields.Many2one('res.users', string='Salesman')
    buyer_id = fields.Many2one('res.partner', string='Buyer', domain=[('is_company', '=', True)])
    buyer_phone = fields.Char(string='Buyer Phone', related='buyer_id.phone')

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for rect in self:
            rect.total_area = rect.garden_area + rect.living_area

    # actions
    def action_sold(self):
        self.state = 'sold'

    def action_cancel(self):
        self.state = 'cancel'

    offer_count = fields.Integer(string="Offer Count", compute='_compute_offer_count')

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for rec in self:
            rec.offer_count = len(rec.offer_ids)

    @api.depends('offer_ids')
    def _compute_best_offer(self):
        for rec in self:
            if rec.offer_ids:
                self.best_offer_price = max(rec.offer_ids.mapped('price'))
            else:
                self.best_offer_price = 0

    def _get_report_base_filename(self):
        self.ensure_one()
        return 'Estate Property - %s' % self.name

    def _compute_website_url(self):
        for rec in self:
            rec.website_url = f'/properties/{rec.name}'

    def _expand_estate(self, states, domain, order):
        return [
            key for key, dummy in type(self).state.selection
        ]

    # def action_url_action(self):
    #     return {
    #         'type': 'ir.actions.act_url',
    #         'url': 'https://odoo.com',
    #         'target': 'new'  # new and self-> open in the current tab
    #     }


    # def action_property_view_offers(self):
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'res_model': 'estate.property.offer',
    #         'name': f'{self.name} - Offers',
    #         'domain': [('property_id', '=', self.id)],
    #         'view_mode': 'tree',
    #     }


class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = "Define the type of property"
    name = fields.Char(string='Property Type')


class PropertyTag(models.Model):
    _name = 'estate.property.tags'
    _description = "Categoruize property with tags"

    name = fields.Char(string='Tag')
    color = fields.Integer(string="Color")
