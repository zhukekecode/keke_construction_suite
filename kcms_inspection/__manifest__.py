# -*- coding: utf-8 -*-
{
    'name': "kcms_inspection",

    'summary': """
        Construction inspection module of KCMS(KEKE Construction Project Management System)
        """,

    'description': """
        Construction inspection module of KCMS(KEKE Construction Project Management System)
    """,

    'author': "Lindsay Zhang & Jianzhuo Shen",
    'website': "http://www.zhukeke.co.nz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'keke/Construction',
    'version': '14.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'kcms_project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/kcms_inspection_menuitem.xml',
        # 'views/kcms_inspection_task_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
