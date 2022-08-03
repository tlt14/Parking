
    # -*- coding: utf-8 -*-
{
    'name': "Parking Lot",
    'description': """Hệ thống quản lý bãi xe""",
    'author': "Thai Lam Truong",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'product',
        'hr'
    ],
    'demo': [
        # "demo/demo_data.xml",
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/parking_lot_view.xml',
        'views/parking_vehicle_view.xml',
        'views/parking_ticket_view.xml',
        'views/parking_pricelist_view.xml',
        'views/parking_vehicle_ref.xml',
        'reports/parking_lot_detail.xml',
        'reports/report.xml',
        'wizard/parking_report_view.xml',   
        'views/menu_view.xml',
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
    
}