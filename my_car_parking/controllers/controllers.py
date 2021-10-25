# -*- coding: utf-8 -*-
# from odoo import http


# class MyCarParking(http.Controller):
#     @http.route('/my_car_parking/my_car_parking/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_car_parking/my_car_parking/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_car_parking.listing', {
#             'root': '/my_car_parking/my_car_parking',
#             'objects': http.request.env['my_car_parking.my_car_parking'].search([]),
#         })

#     @http.route('/my_car_parking/my_car_parking/objects/<model("my_car_parking.my_car_parking"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_car_parking.object', {
#             'object': obj
#         })
