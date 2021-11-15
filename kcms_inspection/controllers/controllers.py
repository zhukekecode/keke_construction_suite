# -*- coding: utf-8 -*-
# from odoo import http


# class KcmsInspection(http.Controller):
#     @http.route('/kcms_inspection/kcms_inspection/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kcms_inspection/kcms_inspection/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kcms_inspection.listing', {
#             'root': '/kcms_inspection/kcms_inspection',
#             'objects': http.request.env['kcms_inspection.kcms_inspection'].search([]),
#         })

#     @http.route('/kcms_inspection/kcms_inspection/objects/<model("kcms_inspection.kcms_inspection"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kcms_inspection.object', {
#             'object': obj
#         })
