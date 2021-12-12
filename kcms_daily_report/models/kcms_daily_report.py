# -*- coding: utf-8 -*-

import base64
from odoo import api, fields, models, _, tools


class KCMSDailyReport(models.Model):
    _name = 'kcms.daily.report'
    _description = 'keke construction management system (daily report) -- Daily Report'

    user_id = fields.Many2one('res.users', default=lambda self: self.env.user, string='Submitter')
    submit_date = fields.Datetime(string="Submit Date", default=fields.Datetime.now, require='1')
    working_date = fields.Date(string='Working Date')
    notes = fields.Text(string='Notes')
    list_id = fields.One2many('kcms.daily.report.item', 'list_ids', string='List Records')