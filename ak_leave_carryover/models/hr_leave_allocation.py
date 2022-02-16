# -*- coding: utf-8 -*-
from odoo import models, fields


class HolidaysAllocation(models.Model):
    _inherit = "hr.leave.allocation"

    leave_carryover_id = fields.Many2one('leave.carry.over', string="Carry Overs")
