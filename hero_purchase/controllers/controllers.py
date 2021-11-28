# -*- coding: utf-8 -*-
# from odoo import http


# class HeroPurchase(http.Controller):
#     @http.route('/hero_purchase/hero_purchase/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hero_purchase/hero_purchase/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hero_purchase.listing', {
#             'root': '/hero_purchase/hero_purchase',
#             'objects': http.request.env['hero_purchase.hero_purchase'].search([]),
#         })

#     @http.route('/hero_purchase/hero_purchase/objects/<model("hero_purchase.hero_purchase"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hero_purchase.object', {
#             'object': obj
#         })
