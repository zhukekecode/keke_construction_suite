# -*- coding: utf-8 -*-

from odoo import api, fields, models, _, tools
import datetime
import pytz


class KCMSDailyReport(models.Model):
    _name = 'kcms.daily.report'
    _description = 'keke construction management system (daily report) -- Daily Report'

    user_id = fields.Many2one('res.users', default=lambda self: self.env.user, string='Submitter')
    submit_date = fields.Datetime(string="Submit Date", default=fields.Datetime.now, require='1')
    working_date = fields.Date(string="Working Date",
                               default=lambda self: datetime.datetime.now(pytz.timezone(self.env.user.tz)).date(),
                               require='1')
    notes = fields.Text(string='Notes')
    list_id = fields.One2many('kcms.daily.report.item', 'list_ids', string='List Records')

    # @api.constrains('list_id')
    # def check_list_id(self):
    #     for item in self:
    #         if item.working_hours <= 0:
    #             raise ValidationError('Check your working hours.')
