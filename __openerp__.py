# -*- coding: utf-8 -*-
{
    'name': "SALE_MARYUN",

    'summary': """
        """,

    'description': """
        Sale & account module extended
    """,

    'author': "consulnet & Angel A. Guadarrama B.",
    'website': "http://www.consulnet.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sale',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        'views/account_workflow.xml',
        'views/account_invoice.xml',
        'views/sale_maryun.xml',
        'views/account_filepath.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        '',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
