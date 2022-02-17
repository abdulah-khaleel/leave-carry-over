# -*- coding: utf-8 -*-
################################################################################# 
#
#    Author: Abdullah Khalil. Copyrights (C) 2021-TODAY reserved. 
#
#    You may use this app as per the rules outlined in the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3. 
#    See <http://www.gnu.org/licenses/> for more detials.
#
################################################################################# 

{
    'name': "Time Off Carry Over",   
    'summary': "Manage staff time off carry over",   
    'description': """
        Easily manage and schedule your staff's time off carry-over with this app.
    """,   
    'author': "Abdullah Khalil",
    'website': "https://github.com/abdulah-khaleel",
    'category': 'Time Off',
    'version': '15.0.0.0',
    'depends': ['base','hr_holidays'],
    'data': [
        'security/ir.model.access.csv',
        'views/carryover_views.xml',
        'views/hr_leave_allocation_views.xml',
    ],
    'images': ["static/description/banner.png"],
    'license': 'LGPL-3',
    'application': True,
    'installable': True,
} 
