# -*- coding: utf-8 -*-
# from odoo import http


# class KcmsDailyReport(http.Controller):
#     @http.route('/kcms_daily_report/kcms_daily_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kcms_daily_report/kcms_daily_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kcms_daily_report.listing', {
#             'root': '/kcms_daily_report/kcms_daily_report',
#             'objects': http.request.env['kcms_daily_report.kcms_daily_report'].search([]),
#         })

#     @http.route('/kcms_daily_report/kcms_daily_report/objects/<model("kcms_daily_report.kcms_daily_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kcms_daily_report.object', {
#             'object': obj
#         })
