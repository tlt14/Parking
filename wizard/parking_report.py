from odoo import api, models, fields

class ParkingReportWizard(models.Model):
    _name = 'parking.report.wizard'
    _description = 'Parking Report Wizard'
    parking_lot_id = fields.Many2one('parking.lot',string = 'Parking Lot',help = 'Select Parking Lot or Vehicle')
    vehicle_id = fields.Many2one('parking.vehicle',string = 'Vehicle', help = 'Select Vehicle or Parking Lot')
    date_from = fields.Date(string = 'Date From')
    date_to = fields.Date(string = 'Date To')

    # onchange method
    @api.onchange('parking_lot_id')
    def onchange_parking_lot_id(self):
        if self.parking_lot_id:
            self.vehicle_id = False
            return {'value': {'vehicle_id': False}}
        
    @api.onchange('vehicle_id')
    def onchange_vehicle_id(self):
        if self.vehicle_id:
            self.parking_lot_id = False
            return {'value': {'parking_lot_id': False}}

    def action_print_report(self):
        form_data =  self.read()[0]
        print("data+++++++++++++++++++++++",form_data)
        if form_data['parking_lot_id']:
            tickets = self.env['parking.ticket'].search_read([('parking_lot_id','=',form_data['parking_lot_id'][0]),('time_start','>=',form_data['date_from']),('time_start','<=',form_data['date_to'])])
        else:
            tickets = self.env['parking.ticket'].search_read([('vehicle_id','=',form_data['vehicle_id'][0]),('time_start','>=',form_data['date_from']),('time_start','<=',form_data['date_to'])])
        data={
            'form': form_data,
            'ticket_count': len(tickets),
            'total_price': sum(ticket['price'] for ticket in tickets),
            'tickets': tickets
        }
        return self.env.ref('parking_lot.action_report_parking').report_action(self, data=data)
    def action_print_xlsx(self):
        form_data =  self.read()[0]
        if form_data['parking_lot_id']:
            tickets = self.env['parking.ticket'].search_read([('parking_lot_id','=',form_data['parking_lot_id'][0]),('time_start','>=',form_data['date_from']),('time_start','<=',form_data['date_to'])])
        else:
            tickets = self.env['parking.ticket'].search_read([('vehicle_id','=',form_data['vehicle_id'][0]),('time_start','>=',form_data['date_from']),('time_start','<=',form_data['date_to'])])
        data={
            'form': form_data,
            'ticket_count': len(tickets),
            'total_price': sum(ticket['price'] for ticket in tickets),
            'tickets': tickets
        }
        return self.env.ref('parking_lot.action_report_parking_xlsx').report_action(self, data=data)