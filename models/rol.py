# -*- coding: ISO-8859-1 -*-

from odoo import models, fields, api

class rol(models.Model):
    _name = 'lol.rol'

    name = fields.Char()
    description = fields.Text()
    campeones = fields.One2many('lol.campeones','idrol',string='Campeones')

    
