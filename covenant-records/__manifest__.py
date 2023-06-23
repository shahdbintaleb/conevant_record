# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Covenant records',
    'category': 'covenant Management',
    'summary': '',
    'description': "",
    'version': '1.0',
    'depends': ['base'],
    'data': ['view\covenant_record_views.xml',
             'security\ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
