# -*- coding: utf-8 -*-

from odoo import models, fields, api

class roles(models.Model):
    _name = 'lol.rol'

    name = fields.Char()
    description = fields.Text()
    campeones = fields.One2many('lol.campeones','idrol',string='Campeones')

    
