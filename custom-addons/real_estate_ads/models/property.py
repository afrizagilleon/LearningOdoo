from odoo import fields, models, api


class Property(models.Model):
    _name = 'estate.property'  # the name Model
    _description = 'Property description'

    name = fields.Char(string='Name', required=True)
    type_id = fields.Many2one('estate.property.type', string='Type')
    tags_id = fields.Many2many('estate.property.tags', string='Tags')
    description = fields.Text(string='Description')
    post_code = fields.Char(string='Postcode')
    date_availability = fields.Datetime(string='Available From')
    expected_price = fields.Float(string='Expected Price')
    selling_price = fields.Float(string='Selling Price')
    best_offer_price = fields.Float(string='Best Offer Price')
    bedrooms = fields.Integer(string='Bedrooms')
    living_area = fields.Integer(string='Living Area(sqm)')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage', default=False)
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Selection([
        ('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')
    ], string='Garden Orientation', default='north')

    total_area = fields.Integer(string='Total Area', compute='_compute_total_area')

    # Relations
    offer_ids = fields.Many2many('estate.property.offer',
                                 'property_id',
                                 string='Offers')
    sales_id = fields.Many2one('res.users', string='Salesman')
    buyer_id = fields.Many2one('res.users', string='Buyer')

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for rect in self:
            rect.total_area = rect.garden_area + rect.living_area


class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = "Define the type of property"
    name = fields.Char(string='Property Type')


class PropertyTag(models.Model):
    _name = 'estate.property.tags'
    _description = "Categoruize property with tags"

    name = fields.Char(string='Tag')
