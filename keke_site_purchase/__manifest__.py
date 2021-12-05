# -*- coding: utf-8 -*-
{
    'name': "Hero Purchase",

    'summary': """
        Hero Onsite purchase""",

    'description': """
        Hero Onsite purchase
    """,

    'author': "Lindsay Zhang",
    'website': "http://www.zhukeke.co.nz",


    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'keke/Construction',
    'version': '14.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'analytic',
                'base_setup',
                'mail',
                'portal',
                'rating',
                'resource',
                'web',
                'web_tour',
                'digest',
                'hr',
                'kcms_project',
                ],

    # only loaded in demonstration mode
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/kcms_site_purchase_all_views.xml',
        'views/kcms_site_purchase_my_views.xml',
        'views/kcms_site_purchase_menuitem.xml',
        'views/extension.xml',
        'data/sq.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
