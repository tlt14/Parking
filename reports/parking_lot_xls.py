from odoo import models

class ParkingXlsx(models.AbstractModel):
    _name = 'report.parking_lot.report_parking_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    _description = 'Parking_lot_xlsx'

    def generate_xlsx_report(self, workbook, data, lines):
        # for obj in partners:
        #     report_name = obj.name
        #     # One sheet by partner
        #     sheet = workbook.add_worksheet(report_name[:31])
        #     bold = workbook.add_format({'bold': True})
        #     sheet.write(0, 0, obj.name, bold)
        # print("data+++++++++++++++++",data)
        # print("line+++++++++++++++++",lines)
        sheet = workbook.add_worksheet('Parking')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, 'CODE', bold)
        sheet.write(0, 1, 'Vehicle', bold)
        sheet.write(0, 2, 'Barking Lot', bold)
        sheet.write(0, 3, 'Price', bold)
        row = 1
        col = 0
        for obj in data['tickets']:
            print("obj+++++++++++++++++",obj)           
            sheet.write(row, col, obj['name_seq'])
            sheet.write(row, col + 1, obj['vehicle_id'][1])
            sheet.write(row, col + 2, obj['parking_lot_id'][1])
            sheet.write(row, col + 3, obj['price'])
            row += 1
            col = 0

        sheet.write(row, col, 'Count', bold)
        sheet.write(row, col + 3, data['ticket_count'], bold)
        row += 1
        col = 0
        sheet.write(row, col, 'Total price', bold)
        sheet.write(row, col + 3, data['total_price'], bold)
        
