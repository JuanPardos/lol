# -*- coding: utf-8 -*-
{
    'name': "lol",

    'summary': """
        Sube a challenger como un pro""",

    'description': """
        Relacion 1-N entre Roles principales y Campeones
    """,

    'author': "Juan Pardos Zarate",
    'website': "https://twitter.com/Juanpzar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','baseModule'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
