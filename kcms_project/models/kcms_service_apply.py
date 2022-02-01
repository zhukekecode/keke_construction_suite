# -*- coding: utf-8 -*-
# Last Modify Date: 18 January 2022
# Author: Lindsay
from odoo import api, fields, models, _, tools


class KCMSProjectMustDo(models.Model):
    _name = "kcms.project.must.do"
    _description = "keke construction management system (must do list) -- must do list"

    list_ids = fields.Many2one("kcms.project", string="Must Do List: ")
    task_ids = fields.Many2one("kcms.project.must.do.tasks", string="Task")
    task_status = fields.Selection(
        selection=[
            ('Yes', 'Yes'),
            ('Pending', 'Pending'),
            ('No', 'No'),
            ('NA', 'NA'),
        ], string="Task Status"
    )

    comp_date = fields.Date(string="Completion Date")
    principle_user = fields.Many2one('res.users', string='People in charge')
    comment = fields.Text(string="Comment")

    @api.onchange('comp_date', 'comment')
    def _onchange_principle_user(self):
        self.principle_user = self.env.user
