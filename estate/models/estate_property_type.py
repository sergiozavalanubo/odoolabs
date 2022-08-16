
from odoo import fields, models

class EstatePropertyType(models.Model):

    _name = "estate.property.type"
    _description = "Real Estate Property Type"
    _order = "sequence, name"
    
    # Fields
    name = fields.Char("Name", required=True)
    sequence = fields.Integer("Sequence", default=10)
    
    # One2Many
    property_ids = fields.One2many("estate.property", "property_type_id", string="Properties")
    
    