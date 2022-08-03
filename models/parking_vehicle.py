from odoo import models, fields
class Parking_vehicle(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------
    _name = 'parking.vehicle'
    _description = 'Loại xe'
    _order = 'name desc'
    _sql_constraints = [
        ('name_uniq_veh', 'unique(name)', 'Name must be unique!'),
    ]
    # ---------------------------------------- Fields ----------------------------------------------
    name = fields.Char("Name",required=True)
    # ---------------------------------------- Relational Fields-------------------------------------
    park_veh_ref = fields.One2many('parking.vehicle.ref','vehicle_id',string = 'Parking Vehicle')
