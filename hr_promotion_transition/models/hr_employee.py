# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    @api.multi
    @api.depends(
        "promotion_transition_ids",
        "promotion_transition_ids.state",
    )
    def _compute_career_transition(self):
        _super = super(HrEmployee, self)
        _super._compute_career_transition()

    promotion_transition_ids = fields.One2many(
        string="Promotion Transitions",
        comodel_name="hr.promotion_transition",
        inverse_name="employee_id",
    )
