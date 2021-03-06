# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ResCompany(models.Model):
    _inherit = "res.company"

    early_attendance_buffer = fields.Float(
        string="Early Attendance Buffer",
        default=0.0,
        required=True,
    )
    late_attendance_buffer = fields.Float(
        string="Late Attendance Buffer",
        default=0.0,
        required=True,
    )
    schedule_change_confirm_grp_ids = fields.Many2one(
        string="Allowed To Confirm Attendance Schedule Change",
        comodel_name="res.groups",
        relation="rel_company_2_group_schedule_change_confirm",
        column1="company_id",
        column2="group_id",
    )
    schedule_change_approve_grp_ids = fields.Many2one(
        string="Allowed To Approve Attendance Schedule Change",
        comodel_name="res.groups",
        relation="rel_company_2_group_schedule_change_approve",
        column1="company_id",
        column2="group_id",
    )
    schedule_change_cancel_grp_ids = fields.Many2one(
        string="Allowed To Cancel Attendance Schedule Change",
        comodel_name="res.groups",
        relation="rel_company_2_group_schedule_change_cancel",
        column1="company_id",
        column2="group_id",
    )
    schedule_change_restart_grp_ids = fields.Many2one(
        string="Allowed To Approve Attendance Schedule Change",
        comodel_name="res.groups",
        relation="rel_company_2_group_schedule_change_restart",
        column1="company_id",
        column2="group_id",
    )
