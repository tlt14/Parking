from odoo import models, fields, api

class Park_Vehicle(models.Model):
    _name = 'parking.vehicle.ref'
    _description = 'parking.vehicle.ref'

    parking_lot_id = fields.Many2one('parking.lot',string = 'Parking Lot',required=True)
    vehicle_id = fields.Many2one('parking.vehicle',string = 'Vehicle',required=True)
    limit_veh = fields.Integer(string = 'Limit Vehicle',required=True)

    blank = fields.Integer(string = 'Blank',compute = '_compute_blank')
    
    
    @api.depends('parking_lot_id.state_in_count')
    def _compute_blank(self):
        for record in self:
            if record.parking_lot_id:
                record.blank = record.limit_veh - record.parking_lot_id.state_in_count
            else:
                record.blank = 0
    # onchange method
    @api.onchange('parking_lot_id')
    def onchange_parking_lot_id(self):
        if self.parking_lot_id:
            # Lấy ra tất cả loại xe
            vehicles = self.env['parking.vehicle'].search([])
            # Lấy ra loại xe đã nhập giới hạn rồi
            vehicles_self = self.env['parking.vehicle.ref'].search([('parking_lot_id','=',self.parking_lot_id.id)])
            tmp = [] # Tạm thời lưu trữ mã loại xe chưa nhập giới hạn
            tmp1 = [] # Tạm thời lưu trữ mã loại xe đã nhập giới hạn
            for y in vehicles_self:
                if y.vehicle_id.id:
                    tmp1.append(y.vehicle_id.id)
            for x in vehicles:
                if x.id not in tmp1:
                    tmp.append(x.id)
            return {'domain': {'vehicle_id': [('id', 'in', tmp)]}}