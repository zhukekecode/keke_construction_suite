# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kcms_inspection(models.Model):
    _name = 'kcms.inspection'
    _description = 'keke construction management system (inspection) -- Inspection'

    project_id = fields.Many2one("kcms.project.pm", string="Project: ", ondelete='restrict')
    building_concent = fields.Char(string="Building concent num: ")
    date = fields.Date(string="Date: ")
    Address = fields.Char(string="Address: ")





