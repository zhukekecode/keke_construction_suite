# -*- coding: utf-8 -*-
# from odoo import http


# class KekeSitePurchase(http.Controller):
#     @http.route('/keke_site_purchase/keke_site_purchase/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/keke_site_purchase/keke_site_purchase/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('keke_site_purchase.listing', {
#             'root': '/keke_site_purchase/keke_site_purchase',
#             'objects': http.request.env['keke_site_purchase.keke_site_purchase'].search([]),
#         })

#     @http.route('/keke_site_purchase/keke_site_purchase/objects/<model("keke_site_purchase.keke_site_purchase"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('keke_site_purchase.object', {
#             'object': obj
#         })
