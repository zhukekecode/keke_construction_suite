# -*- coding: utf-8 -*-
{
    'name': "kcms_purchase",

    'summary': """
        Purchase module of KCMS(KEKE Construction Project Management System)""",

    'description': """
        Purchase module of KCMS(KEKE Construction Project Management System)""",

    'author': "Lindsay Zhang & Jianzhuo Shen",
    'website': "http://www.zhukeke.co.nz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'keke/Construction',
    'version': '14.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'kcms_project', 'purchase'],

    # always loaded
    'data': [
        'views/kcms_purchase_order_views.xml',
        'views/kcms_purchase_menuitem.xml',
        'views/kcms_purchase_project_inherits_views.xml',
        'views/assets.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'qweb': [
        "static/src/xml/kcms_purchase_dashboard.xml",
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
