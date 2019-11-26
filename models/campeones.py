# -*- coding: utf-8 -*-

from datetime import timedelta
from odoo import models, fields, api, exceptions

class campeones(models.Model):
    _name = 'lol.campeones'

    name = fields.Char(required = True, string='Nombre')
    description = fields.Text(string='Descripción')
    fecha = fields.Date(String='Fecha Lanzamiento')
    idrol = fields.Many2one('lol.rol',string='Rol Principal')
    rework = fields.Many2one('lol.rework','idcampeon')
    AP = fields.Boolean()
    AD = fields.Boolean()

    _sql_constraints = [
    ('name_description_check',
        'CHECK(name != description)',
        "La descripción del campeón no puede coincidir con el nombre"),

    ('name_unique',
        'UNIQUE(name)',
        "Ya existe un campeón con ese nombre"),
    ]
     
 

    
