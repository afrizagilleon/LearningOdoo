from odoo import fields, models


class Property(models.Model):
    _name = 'estate.property'  # the name Model
    _description = 'Property description'

    name = fields.Char(string='Name', required=True)
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

    # will be explained soon 
    # id, create_date, create_uid, write_date, write_uid
    
