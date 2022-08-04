from datetime import date, datetime, tzinfo 
from odoo import models, fields, api
import pytz
class Parking_lot(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------
    _name='parking.lot'
    _description='parking.lot'
    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'Name must be unique!'),
    ]

    # ---------------------------------------- Fields ----------------------------------------------
    name = fields.Char(default='Parking')
    # Computed
    state_in_count = fields.Integer(compute = '_state_in_count')
    
    #--------------------------------------- Relational Fields-------------------------------------
    # bãi xe -> park_veh -> loại xe
    # 1 bãi xe có nhiều loại xe
    vehicle_ids = fields.One2many('parking.vehicle.ref','parking_lot_id',string = 'Vehicle')    

    # bãi xe -> price_list
    pricelist_id = fields.Many2one('parking.pricelist',string = 'Pricelist')

    # một bãi xe có nhiều vé xe 
    ticket_ids = fields.One2many('parking.ticket','parking_lot_id',string = 'Ticket')

    resource_calendar = fields.Many2one('resource.calendar',string = 'Resource Calendar')

    #--------------------------------------Actions-------------------------------- 
    def action_show_tickets(self):
        return {
            'name': ('Tickets'),
            'res_model': 'parking.ticket',
            'view_mode': 'list,form',
            'type': 'ir.actions.act_window',
            'domain': [('parking_lot_id','=',self.id)],
            'context': {'search_default_state_filter': 1 }
        }

    # ---------------------------------------- Computed Methods ------------------------------------------------
    @api.depends('ticket_ids')
    def _state_in_count(self):
        for rec in self:
            rec.state_in_count = len([x for x in rec.ticket_ids if x.state == 'in'])
    
    
    # -------------------------------Methods----------------------------------------------------
    def working_time(self):
        # set timezone VietNamese
        timezone = 'Asia/Ho_Chi_Minh'
        # get timezone
        tz = pytz.timezone(timezone)
        # get current time
        now = datetime.now(tz)

        data= self.env['resource.calendar.attendance'].search([('calendar_id','=',self.resource_calendar.id),('dayofweek','=',date.weekday(date.today()))])
        # print("week=================",data)
        x=[x.hour_from for x in data]
        # print("x=================",x)
        y=[x.hour_to for x in data]
        # print("y=================",y)
        for i in range(len(x)):
            if x[i]<=now.hour+(now.minute /60)<=y[i]:
                return True
        return False

    
