# -*- coding: utf-8 -*-
{
    'name': "Sparkit: Sparkit ACA/Spark Logo",

    'summary': """
        Adds Spark MicroGrants/ACA logo to topbar.""",

    'description': """
        Adds Spark MicroGrants/ACA logo to topbar.
    """,

    'author': "Spark MicroGrants",
    'website': "http://www.sparkmicrogrants.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sparkit'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
