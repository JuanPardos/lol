# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class rol(models.Model):
    _name = 'lol.rol'

    name = fields.Char()
    description = fields.Text()
    campeones = fields.One2many('lol.campeones','idrol',string='Campeones')
    nerf = fields.Boolean(default=False,string='Ha sido nerfeado este año')

    _sql_constraints = [
    ('name_description_check',
        'CHECK(name != description)',
        "La descripción del rol no puede coincidir con el nombre"),

    ('name_unique',
        'UNIQUE(name)',
        "Ya existe un rol con ese nombre"),
    ]        
    
