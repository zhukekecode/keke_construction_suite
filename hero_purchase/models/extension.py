from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

class EmpExtension(models.Model):
    _name = "hr.employee"
    _inherit = "hr.employee"

    purchase_code_prefix = fields.Char(string="Purchase Code Prefix")
    purchase_code_offset = fields.Integer()

    # @api.constrains('purchase_code_prefix')
    # def check_purchase_code_prefix(self):
    #     if len(str(self.purchase_code_prefix)) == 0:
    #         raise ValidationError('Please set your PO Number.')
