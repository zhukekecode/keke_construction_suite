# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime
import pytz
from odoo.exceptions import ValidationError, UserError, Warning


class HeroPurchaseSite(models.Model):
    _name = 'hero_purchase.site'
    _inherit = ['mail.thread']
    _description = '工地采购实体类'

    name = fields.Char(string="PO Number")
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user, string='Submitter')
    note = fields.Char(string="Notes")
    purchase_date = fields.Date(string="Purchase Date",
                                default=lambda self: datetime.datetime.now(pytz.timezone(self.env.user.tz)).date(),
                                require='1')
    # submit_date = fields.Datetime(string="Submit Date", default=fields.Datetime.now, require='1')
    submit_date = fields.Date(string="Submit Date",
                              default=lambda self: datetime.datetime.now(pytz.timezone(self.env.user.tz)).date(),
                              require='1')
    item_ids = fields.One2many('hero_purchase.site_item', 'purchase_id', string='Purchase Items')
    status = fields.Selection(
        [('to_process', '进行中'), ('is_completed', '已完成'), ('Approved', '已审批')],
        string="status", default='to_process')
    attachment_id = fields.Many2many('ir.attachment', string="Invoice")

    @api.model
    def create(self, vals):
        record = super(HeroPurchaseSite, self).create(vals)
        print(record)
        """
        自动生成PO No.
        """

        if record.user_id.employee_id.purchase_code_prefix:
            offset = str(record.user_id.employee_id.purchase_code_offset + 1).rjust(3, "0")
            record.name = (record.user_id.employee_id.purchase_code_prefix + offset) or ''
            record.user_id.employee_id.purchase_code_offset = record.user_id.employee_id.purchase_code_offset + 1
        else:
            raise ValidationError('Please set your PO Number.')
        return record

    # 已完成状态下不能修改单据
    def write(self, vals):
        ctx = dict(self._context or {})
        if self.status == "Approved":
            raise ValidationError(u"审批完成单据不能修改! This record cannot be modified in the completed state")
        return super(HeroPurchaseSite, self.with_context(ctx)).write(vals)


class HeroPurchaseSiteList(models.Model):
    _name = 'hero_purchase.site_item'
    _description = '工地采购明细实体类'

    item = fields.Char(string="Item")
    price = fields.Float(string="Unit Price")
    unit = fields.Char(string="Unit")
    quantity = fields.Integer(string="Quantity")
    purchase_id = fields.Many2one("hero_purchase.site", string='Purchase Order', ondelete='cascade')
    project_id = fields.Many2one("construction.project", string='Project', ondelete='restrict')
    task_id = fields.Many2one('construction.task', string='Task', domain=[('project_id', '=', project_id)])

    @api.onchange('price')
    def check_price(self):
        if self.price < 0:
            raise ValidationError('Please check the price.')

    @api.onchange('project_id')
    def _onchange_project_id(self):
        self.task_id = False
        if self.project_id:
            return {'domain': {'task_id': [('project_id', '=', self.project_id.id), ('status', '=', 'to_process'),
                                           ('task_id', '!=', False)]}}
        else:
            return {'domain': {'task_id': [('name', '=', False)]}}
