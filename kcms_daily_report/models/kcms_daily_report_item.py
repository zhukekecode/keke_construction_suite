# -*- coding: utf-8 -*-

import base64
from odoo import api, fields, models, _, tools
from odoo.api import onchange
import datetime
import pytz
from odoo.exceptions import ValidationError, UserError


class KCMSDailyReportItem(models.Model):
    _name = 'kcms.daily.report.item'
    _description = 'keke construction management system (daily report) -- Daily Report'

    list_ids = fields.Many2one('kcms.daily.report', string='List Item', ondelete='cascade')
    kcms_project_id = fields.Many2one("kcms.project", string="Project", ondelete='cascade')
    kcms_project_item_base_id = fields.Many2one("kcms.project.item.base", string="Task", ondelete='restrict', required='1')
    working_hours = fields.Float(string="Total Time", required='1', group_operator=False)
    user_ids = fields.Many2many('hr.employee', string='Group Members',
                                domain=[('department_id.name', '=', 'Construction')])

    @api.constrains('working_hours')
    def check_work_hours(self):
        for item in self:
            if item.working_hours <= 0 or item.working_hours > 24:
                raise ValidationError('Check your working hours.')
