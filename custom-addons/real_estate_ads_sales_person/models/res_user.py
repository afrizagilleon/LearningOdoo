from odoo import api, fields, models


class Users(models.Model):
    _inherit = 'res.users'

    property_ids = fields.Many2many('estate.property', 'sales_id',
                                    string="Properties")