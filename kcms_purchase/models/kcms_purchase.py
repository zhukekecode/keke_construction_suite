from odoo import api, fields, models, _, tools
from odoo.api import onchange
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError


class KCMSPurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    kcms_project_item_id = fields.Many2one("kcms.project.item", string="Item Code", ondelete='restrict')
    kcms_project_id = fields.Many2one("kcms.project.pm", string="Project Code", ondelete='restrict')
    kcms_project_item_base_id = fields.Many2one("kcms.project.item.base", string="Item Base", ondelete='restrict')

    @onchange('kcms_project_item_id')
    def _onchange_item(self):
        if self.kcms_project_item_id:
            self.kcms_project_id = self.kcms_project_item_id.project_id.id
            self.kcms_project_item_base_id = self.kcms_project_item_id.base_id.id

    @api.model
    def get_dashboard_data(self, domains):
        """ This function returns the values to populate the custom dashboard in
                    the purchase order views.
                """
        result = {
            'order_value': 0,
            'bill_value': 0,
            'est_cost': 0,
            'order_counts': 0,
            'company_currency_symbol': self.env.company.currency_id.symbol,
        }

        kpib_id = 0
        kp_id = 0
        item = None
        if domains:
            for domain in domains:
                if domain[0] == 'kcms_project_id':
                    kp_id = domain[2]
                elif domain[0] == 'kcms_project_item_base_id':
                    kpib_id = domain[2]
            print(kpib_id, kp_id)
            if kpib_id and kp_id:
                item = self.env['kcms.project.item'].search([('project_id', '=', kp_id), ('base_id', '=', kpib_id)])
            if item:
                print(item)
                if item.total_order_value:
                    result["order_value"] = item.total_order_value

        return result
