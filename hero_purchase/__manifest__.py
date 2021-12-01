# -*- coding: utf-8 -*-
{
    'name': "Hero Purchase",

    'application': True,

    'summary': """
       Hero 工地采购明细模块""",

    'description': """
        Hero 工地采购明细模块
    """,

    'author': "Hero--Lindsay",
    'website': "http://www.herointernational.co.nz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'keke/Construction',
    'version': '14.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'construction'],

    # always loaded
    'data': [
        'data/sq.xml',
        'security/hero_purchase_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/extension.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
