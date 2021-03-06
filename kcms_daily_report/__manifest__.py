# -*- coding: utf-8 -*-
{
    'name': "Daily Report",

    'summary': """
        Project module of KCMS(KEKE Construction Project Daily Report System)""",

    'description': """
        Project module of KCMS(KEKE Construction Project Daily Report System)
    """,

    'author': "Lindsay Zhang & Jianzhuo Shen",
    'website': "http://www.zhukeke.co.nz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'keke/Construction',
    'version': '14.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'kcms_project',
                'hr',
                ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/kcms_daily_report_security.xml',
        'views/kcms_daily_report_all_views.xml',
        'views/kcms_daily_report_my_views.xml',
        'views/kcms_daily_report_menuitem.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
