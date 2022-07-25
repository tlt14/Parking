from odoo import fields, models

class Parking_pricelist_item(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------
    _name = "parking.pricelist.item"
    _description = "Parking_pricelist"
    # ---------------------------------------- Fields ----------------------------------------------
    price = fields.Float(required=True,string = "Price")


    # Relational Fields
    pricelist_id = fields.Many2one('parking.pricelist')
    vehicle_id = fields.Many2one('parking.vehicle',string = 'Vehicle')