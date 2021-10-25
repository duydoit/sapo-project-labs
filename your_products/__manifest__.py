# -*- coding: utf-8 -*-
{
    'name': "Sản phẩm",
    'summary': """Sản phẩm của bạn""" ,
    'description': """ quản lý thông tin sản phẩm """,
    'author': "Duydo",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],


    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
