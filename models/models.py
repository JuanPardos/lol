# -*- coding: ISO-8859-1 -*-

from odoo import models, fields, api

class modelo(models.Model):
    _name = 'lol.modelo'
    _inherit = 'base.entidad'   # Esto es porque depende del base.

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
