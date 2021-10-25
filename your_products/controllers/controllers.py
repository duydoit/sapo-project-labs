# -*- coding: utf-8 -*-
# from odoo import http


# class YourProducts(http.Controller):
#     @http.route('/your_products/your_products/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/your_products/your_products/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('your_products.listing', {
#             'root': '/your_products/your_products',
#             'objects': http.request.env['your_products.your_products'].search([]),
#         })

#     @http.route('/your_products/your_products/objects/<model("your_products.your_products"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('your_products.object', {
#             'object': obj
#         })
