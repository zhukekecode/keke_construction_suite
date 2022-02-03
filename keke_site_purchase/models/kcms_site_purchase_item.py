from odoo import models, fields, api
import datetime
import pytz
from odoo.exceptions import ValidationError, UserError


class KCMSSitePurchaseItem(models.Model):
    _name = 'kcms.site.purchase.item'
    _description = '工地采购明细实体类'

    item = fields.Char(string="Item")
    price = fields.Float(string="Unit Price")
    unit = fields.Char(string="Unit")
    quantity = fields.Integer(string="Quantity")
    purchase_id = fields.Many2one("kcms.site.purchase", string="Purchase Order", ondelete="cascade")
    kcms_project_id = fields.Many2one("kcms.project.pm", string="Project", ondelete="restrict")
    kcms_project_item_base_id = fields.Many2one("kcms.project.item.base", string='Task')

    @api.onchange('price')
    def check_price(self):
        if self.price < 0:
            raise ValidationError('Please check the price.')
