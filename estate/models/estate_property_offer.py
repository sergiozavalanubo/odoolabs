
from odoo import fields, models

class EstatePropertyOffer(models.Model):

    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"
    
    # Fields
    price = fields.Float("Price", required=True)
    
    # Fases
    state = fields.Selection(
        selection=[
            ("accepted", "Accepted"),
            ("refused", "Refused"),
        ],
        string="Status",
        copy=False,
        default=False,
    )

    # Many2one
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)
    