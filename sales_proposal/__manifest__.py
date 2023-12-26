# -*- coding: utf-8 -*-
{
    'name': 'Sale Proposal',
    'version': '16.0',
    'category': 'Sales',
    'sequence': 1,
    'author' : 'Pankaj Yadav',
    'description': """
Sale Order with Proposal
====================
The goal of this custom module is to manage the proposal of products to the
customer. A Sale Proposal is created and sent to the customer where the
customer can see the proposal on the web, edit the proposal and accept the
proposal. Once the customer accepts the proposal the sales quotation is
created for the same.
    """,
    'website': False,
    'images' : False,
    'depends': ['sale_management'],
    'data': [
        'security/ir.model.access.csv',        
        'report/report_templates.xml',
        'report/reports.xml',
        'data/sale_proposal_sequence.xml',
        'data/proposal_mail_template_data.xml',
        'views/sale_proposal_views.xml',
        'views/sale_proposal_line_views.xml',
        'views/sale_proposal_portal_templates.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            'sale_proposal/static/src/js/sale_proposal_portal.js',
            'sale_proposal/static/src/xml/**/*',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,

}
