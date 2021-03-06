# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    password_expiration = fields.Integer(
        'Days', default=60, help='How many days until passwords expire'
    )
    password_length = fields.Integer(
        'Characters', default=12, help='Minimum number of characters'
    )
    password_lower = fields.Boolean(
        'Lowercase', default=True, help='Require lowercase letters'
    )
    password_upper = fields.Boolean(
        'Uppercase', default=True, help='Require uppercase letters'
    )
    password_numeric = fields.Boolean(
        'Numeric', default=True, help='Require numeric digits'
    )
    password_special = fields.Boolean(
        'Special', default=True, help='Require special characters'
    )
