from datetime import date
import math
import re
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
class Parking_ticket(models.Model):
    _name = 'parking.ticket'
    _description = 'parking.ticket'

    # ---------------------------------------- Fields ----------------------------------------------
    # Code
    name_seq = fields.Char('Ticket Number',required=True,readonly=True, copy=False, default='New')
    
    image = fields.Image(string="Image")
    time_start = fields.Datetime('Time start',default = lambda self: fields.Datetime.now())
    time_end = fields.Datetime('Time end',readonly=True)
    total_time = fields.Char('Total time',readonly=True)
    state = fields.Selection(
        string='State',
        selection=[('in', 'In'), ('out', 'Out'),],
        default='in',
        readonly=True,
        index=True,
    )

    # Relational Fields
    # nhiều vé xe nằm trong một bãi xe
    parking_lot_id = fields.Many2one('parking.lot',required=True,default= lambda self: self.env.context.get('active_id'))
    vehicle_id = fields.Many2one('parking.vehicle')

    pricelist_id = fields.Many2one(related = 'parking_lot_id.pricelist_id', store=True)
    price = fields.Float('Price',readonly=True)


    # ---------------------------------------- CRUD Methods --------------------------------
    @api.model
    def create(self, vals):
        if vals.get('name_seq', 'New') == 'New':
            today = fields.Date.today()
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('project.task')+str(today.day)+str(today.month)+str(today.year) or 'New'       
        parking_lot = self.env['parking.lot'].search([('id','=',vals['parking_lot_id'])]).working_time()
        if parking_lot == False:
            raise UserError('Parking lot is not working')
        elif self.env['parking.vehicle.ref'].search([('vehicle_id','=',vals['vehicle_id']),('parking_lot_id','=',vals['parking_lot_id'])]).blank <= 0:
            raise ValidationError('Parking lot is full')
        else:
            result = super().create(vals)
            return result

    # ---------------------------------------- Actions Methods --------------------------------
    def action_finish(self):
        self.time_end = fields.Datetime.now()
        duration = self.time_end - self.time_start
        duration_in_s = duration.total_seconds() 
        minutes = divmod(duration_in_s, 60)[0]
        hours = divmod(duration_in_s, 3600)[0]+round(( minutes % 60 )/60, 2)
        if hours < 1 and minutes < 60:
            if( ( minutes % 60 )/60 >= 0.5 ):
                hours = math.ceil(hours) 
                self.total_time = str(hours) +" hours"
            else:
                self.total_time = str(minutes)+" minutes"
        else:
            if( ( minutes % 60 )/60 >=0.5 ):
                hours = math.ceil(hours)   
            self.total_time = str(hours) +" hours"

        tmp = self.env['parking.pricelist.item'].search([('pricelist_id','=',self.pricelist_id.id),('vehicle_id','=',self.vehicle_id.id)])
        self.price = tmp.price * hours
        self.state = 'out'

        
