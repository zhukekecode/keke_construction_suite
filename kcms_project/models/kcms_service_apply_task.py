# -*- coding: utf-8 -*-
# Last Modify Date: 18 January 2022
# Author: Lindsay
from odoo import api, fields, models, _, tools


class KCMSProjectMustDoTasks(models.Model):
    _name = "kcms.project.must.do.tasks"
    _description = "keke construction management system (must do list tasks) -- must do list tasks"

    name = fields.Char(string="name")
    sequence = fields.Integer(string='Sequence')
