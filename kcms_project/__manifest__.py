# -*- coding: utf-8 -*-
{
    'name': "kcms_project",

    'summary': """
        Project module of KCMS(KEKE Construction Project Management System)""",

    'description': """
        Project module of KCMS(KEKE Construction Project Management System)""",

    'author': "Lindsay Zhang & Jianzhuo Shen",
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
                ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/kcms_project_security.xml',
        'views/kcms_project_views.xml',
        'views/kcms_project_item_base_views.xml',
        'views/kcms_project_item_views.xml',
        'views/kcms_project_menuitem.xml',
        'views/assets.xml',
        'data/project_mustdo_data.xml',
        'data/hr_department_data.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [
        "static/src/xml/widget_template.xml",
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
