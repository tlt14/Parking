from odoo import models, fields, api

class Park_Vehicle(models.Model):
    _name = 'parking.vehicle.ref'
    _description = 'parking.vehicle.ref'

    parking_lot_id = fields.Many2one('parking.lot',string = 'Parking Lot')
    vehicle_id = fields.Many2one('parking.vehicle',string = 'Vehicle')
    limit_veh = fields.Integer(string = 'Limit Vehicle')

    