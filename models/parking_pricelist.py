from odoo import fields, models

class Parking_pricelist(models.Model):
    _name = "parking.pricelist"
    _description = "Parking_pricelist"
    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'Name must be unique!'),
    ]

    name = fields.Char(required=True,string = "Name")

    vehicle_id = fields.Many2one('parking.vehicle',string = 'Vehicle')
    pricelist_item_ids = fields.One2many('parking.pricelist.item','pricelist_id',string = 'Pricelist Item')

    