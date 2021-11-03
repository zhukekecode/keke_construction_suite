# -*- coding: utf-8 -*-
# from odoo import http


# class KekeConstruction(http.Controller):
#     @http.route('/keke_construction/keke_construction/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/keke_construction/keke_construction/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('keke_construction.listing', {
#             'root': '/keke_construction/keke_construction',
#             'objects': http.request.env['keke_construction.keke_construction'].search([]),
#         })

#     @http.route('/keke_construction/keke_construction/objects/<model("keke_construction.keke_construction"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('keke_construction.object', {
#             'object': obj
#         })
