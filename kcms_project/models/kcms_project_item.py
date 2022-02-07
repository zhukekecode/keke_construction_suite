# -*- coding: utf-8 -*-
from odoo import fields, models


class KCMSProjectItemBase(models.Model):
    _name = "kcms.project.item.base"
    _description = "keke construction management system (project) -- ItemBase"
    # _rec_name = 'name_path'

    sequence = fields.Integer(string='Sequence')
    code = fields.Char(string="Item Code")
    name = fields.Char(string="Item Name", translate=True)
    description = fields.Char(string="Item Description")
    UOM = fields.Char(string="UOM", default="N/A")
    itembase_id = fields.Many2one("kcms.project.item.base", string="Parent Item", ondelete='cascade')
    itembase_ids = fields.One2many('kcms.project.item.base', 'itembase_id', string='Sub Item')
    daily_report = fields.Boolean(string='Daily Report', default=True)
    site_purchase = fields.Boolean(string='Site Purchase', default=True)


class KCMSProjectItem(models.Model):
    _name = "kcms.project.item"
    _description = "keke construction management system (project) -- Item"
    # _rec_name = 'name_path'

    sequence = fields.Integer(string='Sequence')
    code = fields.Char(string="Code")
    project_id = fields.Many2one("kcms.project.pm", string="Project", ondelete='restrict')
    base_id = fields.Many2one("kcms.project.item.base", string="Item", ondelete='restrict')
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id')
    estimate_cost = fields.Monetary('Estimate Cost', currency_field='currency_id', default=0.0)
    subitem_ids = fields.One2many('kcms.project.subitem', 'item_id', string='Subitems')


class KCMSProjectSubitem(models.Model):
    _name = "kcms.project.subitem"
    _description = "keke construction management system (project) -- Subitem"
    # _rec_name = 'name_path' # 改过了

    sequence = fields.Integer(string='Sequence')
    base_id = fields.Many2one("kcms.project.item.base", string="Item", ondelete='restrict')
    quantity = fields.Float(string='Quantity', default=0.0)
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id')
    rate = fields.Monetary('Rate', currency_field='currency_id', default=0.0)
    sub_total = fields.Monetary('Sub Total', currency_field='currency_id')
    item_id = fields.Many2one("kcms.project.item", string="Item", ondelete='cascade')
