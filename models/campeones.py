# -*- coding: utf-8 -*-

from odoo import models, fields, api

class campeones(models.Model):
    _name = 'lol.campeones'

    name = fields.Char()
    description = fields.Text()
    idrol = fields.Many2one('lol.rol',string='Rol Principal')

    
