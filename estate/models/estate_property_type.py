
from odoo import fields, models

class EstatePropertyType(models.Model):

    _name = "estate.property.type"
    _description = "Real Estate Property Type"
    _order = "name"
    
    # Fields
    name = fields.Char("Name", required=True)
    
    # One2Many
    property_ids = fields.One2many("estate.property", "property_type_id", string="Properties")
    
    