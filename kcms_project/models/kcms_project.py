# -*- coding: utf-8 -*-
import base64
import xlrd
from odoo import api, fields, models, _, tools
from odoo.api import onchange
import datetime
import pytz
from odoo.exceptions import ValidationError, UserError


class KCMSProject(models.Model):
    _name = "kcms.project"
    _description = "keke construction management system (project) -- project"
    _parent_name = "project_id"
    _parent_store = True
    _rec_name = 'code'

    sequence = fields.Integer(string='Sequence')
    active = fields.Boolean(default=True,
                            help="If the active field is set to False, it will allow you to hide the project without removing it.")
    code = fields.Char(string="Project Code: ")
    name = fields.Char(string="Project/Block: ")
    name_path = fields.Char(string="Internal Ref.: ", compute='_compute_name_path', store=True)
    project_id = fields.Many2one("kcms.project", string="Parent Project: ", ondelete='restrict')
    project_ids = fields.One2many('kcms.project', 'project_id', string='Sub Projects: ')
    parent_path = fields.Char(index=True)
    user_id = fields.Many2one('res.users', string='Project Manager: ', tracking=True)
    attachment_number = fields.Integer('Number of Attachments', compute='_compute_attachment_number')
    item_ids = fields.One2many('kcms.project.must.do', 'list_ids', string='test**')
    ## Project/Block Informtion
    partner_id_owner = fields.Char(string='Name of owner: ')
    partner_id_FPC = fields.Char(string='Full name: ')
    contact_person = fields.Char(string="Contact Person: ")
    project_address = fields.Char(string="Address: ")
    project_name = fields.Char(string="Project Name: ")
    building_work = fields.Char(string="Building work: ")
    block_work = fields.Char(string="Block work: ")
    building_concent = fields.Char(string="BCO: ")
    lot_range = fields.Char(string="Lot Range: ")
    start_date = fields.Date(string="Start Date: ")
    estimated_completion_date = fields.Date(string="Est. Completion Date: ")
    rc_number = fields.Char(string="R.C. No.")
    EPA = fields.Char(string="EPA: ")

    mailing_address = fields.Char(string="Mailing address: ")
    email_address = fields.Char(string="Email address: ")
    street_address = fields.Char(string="Street address/ registered office: ")
    day_time_phone = fields.Char(string="Day time phone: ")
    mobile_number = fields.Char(string="Mobile: ")
    after_hours = fields.Char(string="After hours: ")
    facsimile = fields.Char(string="Facsimile: ")
    comments = fields.Char(string="Comments: ")
    list_id = fields.One2many('kcms.project.must.do', 'list_ids', string='List Tasks')

    user_ids = fields.Many2many('hr.employee', string='Project Managers: ',
                                domain=[('department_id.name', '=', 'Construction')])
    status = fields.Selection(
        [('to_planning', '规划中'), ('to_process', '进行中'), ('is_completed', '已竣工')],
        string="项目状态", default='to_process')

    # Our Project Manager
    @api.model
    def create(self, vals):
        res = super(KCMSProject, self).create(vals)
        if not vals['project_id']:
            self.env['kcms.project'].create({
                'code': res.code + 'GE',
                'name': 'General',
                'project_id': res.id,
            })
            print(self.env['kcms.project.must.do.tasks'].search([]))
            for task in self.env['kcms.project.must.do.tasks'].search([]):
                self.env['kcms.project.must.do'].create({
                    'list_ids': res.id,
                    'task_ids': task.id,
                })
        return res

    @onchange('code', 'project_id')
    def _onchange_code(self):
        if self.project_id:
            if self.project_id.code not in self.code:
                self.code = self.project_id.code + self.code

    def action_get_attachment_view(self):
        self.ensure_one()
        res = self.env['ir.actions.act_window']._for_xml_id('base.action_attachment')
        rids = self.ids
        if self.project_ids:
            for p in self.project_ids:
                rids = rids + p.ids
        res['domain'] = [('res_model', '=', 'kcms.project'), ('res_id', 'in', rids)]
        res['context'] = {'default_res_model': 'kcms.project', 'default_res_id': self.id}
        return res

    @api.depends('name', 'project_id.name_path')
    def _compute_name_path(self):
        for project in self:
            if project.project_id:
                project.name_path = '%s / %s' % (project.project_id.name_path, project.name)
            else:
                project.name_path = project.name

    def _compute_attachment_number(self):
        attachment_data = self.env['ir.attachment'].read_group(
            [('res_model', '=', 'kcms.project'), ('res_id', 'in', self.ids)], ['res_id'], ['res_id'])
        attachment = dict((data['res_id'], data['res_id_count']) for data in attachment_data)
        for expense in self:
            expense.attachment_number = attachment.get(expense.id, 0)
        if self.project_ids:
            for p in self.project_ids:
                self.attachment_number = self.attachment_number + p.attachment_number

    def create_item_from_attachments(self, attachment_ids=None, pid=None, view_type='tree'):
        if attachment_ids is None:
            attachment_ids = []
        attachments = self.env['ir.attachment'].browse(attachment_ids)
        pid = self.env['kcms.project'].browse(pid)
        if not attachments:
            raise UserError(_("No attachment was provided"))

        for attachment in attachments:
            decoded_data = base64.b64decode(attachment.datas)
            book = xlrd.open_workbook(file_contents=decoded_data or b'')
            sh = book.sheet_by_index(0)
            sub_items = []
            is_start = False
            base_id = None
            item = None
            for rx in range(0, sh.nrows):
                row = sh.row(rx)
                if row[0].value.isdigit():
                    is_start = True
                    self.create_subitems(base_id, item, sub_items)
                    code = row[0].value
                    name = row[1].value
                    base_id = self.env['kcms.project.item.base'].search([('code', '=', code)])
                    if not base_id.code:
                        base_id = self.env['kcms.project.item.base'].create({
                            'code': code,
                            'name': name,
                        })
                    item = self.env['kcms.project.item'].create({
                        'code': pid.code + base_id.code,
                        'project_id': pid.id,
                        'base_id': base_id.id,
                    })
                    sub_items = []
                elif is_start:
                    sub_items.append(row)
            print(base_id, item, sub_items)
            self.create_subitems(base_id, item, sub_items)

    def create_subitems(self, base_id, item, sub_items):
        for sub_item in sub_items:
            if sub_item[1].value:
                if sub_item[0].value:
                    quantity = 0 if sub_item[2].value == '' else sub_item[2].value
                    rate = 0 if sub_item[4].value == '' else sub_item[4].value
                    sub_total = float(quantity) * float(rate)

                    subbase_id = self.env['kcms.project.item.base'].search([('code', '=', sub_item[0].value)])
                    if not subbase_id.code:
                        subbase_id = self.env['kcms.project.item.base'].create({
                            'code': sub_item[0].value,
                            'name': sub_item[1].value,
                            'itembase_id': base_id.id,
                            'UOM': str(sub_item[3].value),
                        })

                    self.env['kcms.project.subitem'].create({
                        'base_id': subbase_id.id,
                        'quantity': format(quantity, '.2f'),
                        'rate': format(rate, '.2f'),
                        'sub_total': format(sub_total, '.2f'),
                        'item_id': item.id,
                    })


class KCMSProjectMustDo(models.Model):
    _name = "kcms.project.must.do"
    _description = "keke construction management system (must do list) -- must do list"

    list_ids = fields.Many2one("kcms.project", string="Must Do List: ")
    task_ids = fields.Many2one("kcms.project.must.do.tasks", string="Task")
    task_status = fields.Selection(
        selection=[
            ('Yes', 'Yes'),
            ('Pending', 'Pending'),
            ('No', 'No'),
            ('NA', 'NA'),
        ], string="Task Status"
    )

    comp_date = fields.Date(string="Completion Date")
    principle_user = fields.Many2one('res.users', string='People in charge')
    comment = fields.Text(string="Comment")

    @api.onchange('comp_date', 'comment')
    def _onchange_principle_user(self):
        self.principle_user = self.env.user


class KCMSProjectMustDoTasks(models.Model):
    _name = "kcms.project.must.do.tasks"
    _description = "keke construction management system (must do list tasks) -- must do list tasks"

    name = fields.Char(string="name")
    sequence = fields.Integer(string='Sequence')
