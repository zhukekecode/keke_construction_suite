from odoo import models, fields, api
import datetime
import pytz
from odoo.exceptions import ValidationError, UserError


class KCMSSitePurchase(models.Model):
    _name = 'kcms.site.purchase'
    _inherit = ['mail.thread']
    _description = '工地采购实体类'

    po_number = fields.Char(string="PO Number")
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user, string='Submitter')
    note = fields.Char(string="Notes")
    purchase_date = fields.Date(string="Purchase Date",
                                default=lambda self: datetime.datetime.now(pytz.timezone(self.env.user.tz)).date(),
                                require='1')
    submit_date = fields.Date(string="Submit Date",
                              default=lambda self: datetime.datetime.now(pytz.timezone(self.env.user.tz)).date(),
                              require='1')
    item_ids = fields.One2many('kcms.site.purchase.item', 'purchase_id', string='Purchase Items')
    status = fields.Selection([('to_process', '进行中'), ('is_completed', '已完成'), ('Approved', '已审批')],string="status", default='to_process')
    attachment_id = fields.Many2many('ir.attachment', string="Invoice")

    @api.model
    def create(self, vals):
        record = super(KCMSSitePurchase, self).create(vals)
        print(record)
        """
        自动生成PO No.
        """
        if record.user_id.employee_id.purchase_code_prefix:
            offset = str(record.user_id.employee_id.purchase_code_offset + 1).rjust(3, "0")
            record.po_number = (record.user_id.employee_id.purchase_code_prefix + offset) or ''
            record.user_id.employee_id.purchase_code_offset = record.user_id.employee_id.purchase_code_offset + 1
        else:
            raise ValidationError('Please set your PO Number.')
        return record

    # #已完成状态下不能修改单据
    # def write(self, vals):
    #     ctx = dict(self._context or {})
    #     if self.status == "Approved":
    #         raise ValidationError(u"审批完成单据不能修改! This record cannot be modified in the completed state")
    #     return super(KCMSSitePurchase, self.with_context(ctx)).write(vals)
