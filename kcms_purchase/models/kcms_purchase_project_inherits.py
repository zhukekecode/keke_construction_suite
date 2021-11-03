from odoo import api, fields, models, _, tools
from odoo.api import onchange
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError


class KCMSPurchaseProjectItemInherit(models.Model):
    _inherit = 'kcms.project.item'

    kcms_purchase_order_ids = fields.One2many('purchase.order', 'kcms_project_item_id', string='Sub Projects')
    total_order_value = fields.Monetary('Total Order Value', currency_field='currency_id', default=0.0, compute='_compute_tov', store=True)

    @api.depends('kcms_purchase_order_ids')
    def _compute_tov(self):
        tov = 0
        if self.kcms_purchase_order_ids:
            for order_id in self.kcms_purchase_order_ids:
                tov += order_id.amount_total
            self.total_order_value = tov

