
from odoo import fields, models

class EstatePropertyType(models.Model):

    _name = "estate.property.tag"
    _description = "Real Estate Property Tag"
    _order = "name"

    # Fields
    name = fields.Char("Name", required=True)    