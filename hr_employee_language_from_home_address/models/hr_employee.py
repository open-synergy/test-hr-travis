# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    language_ids = fields.One2many(
        comodel_name="partner.language",
        related="address_home_id.language_ids",
        string="Languages",
    )
