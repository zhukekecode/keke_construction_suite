# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
from odoo.api import onchange
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError


class KCMSProjectItemBase(models.Model):
    _name = "kcms.project.item.base"
    _description = "keke construction management system (project) -- ItemBase"

    sequence = fields.Integer(string='Sequence')
    code = fields.Char(string="Item Code")
    name = fields.Char(string="Item Name")
    discription = fields.Char(string="Item Discription")
    UOM = fields.Char(string="UOM", default="N/A")
    itembase_id = fields.Many2one("kcms.project.item.base", string="Parent Item", ondelete='cascade')
    itembase_ids = fields.One2many('kcms.project.item.base', 'itembase_id', string='Sub Item')


class KCMSProjectItem(models.Model):
    _name = "kcms.project.item"
    _description = "keke construction management system (project) -- Item"
    _rec_name = 'code'

    sequence = fields.Integer(string='Sequence')
    code = fields.Char(string="Code")
    project_id = fields.Many2one("kcms.project", string="Project", ondelete='restrict')
    base_id = fields.Many2one("kcms.project.item.base", string="Item", ondelete='restrict')
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id')
    estimate_cost = fields.Monetary('Estimate Cost', currency_field='currency_id', default=0.0)
    subitem_ids = fields.One2many('kcms.project.subitem', 'item_id', string='Subitems')


class KCMSProjectSubitem(models.Model):
    _name = "kcms.project.subitem"
    _description = "keke construction management system (project) -- Subitem"
    _rec_name = 'base_id'

    sequence = fields.Integer(string='Sequence')
    base_id = fields.Many2one("kcms.project.item.base", string="Item", ondelete='restrict')
    quantity = fields.Float(string='Quantity', default=0.0)
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id')
    rate = fields.Monetary('Rate', currency_field='currency_id', default=0.0)
    sub_total = fields.Monetary('Sub Total', currency_field='currency_id')
    item_id = fields.Many2one("kcms.project.item", string="Item", ondelete='cascade')


