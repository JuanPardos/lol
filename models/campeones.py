# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class campeones(models.Model):
    _name = 'lol.campeones'

    name = fields.Char(required = True, string='Nombre')
    description = fields.Text(string='Descripción')
    idrol = fields.Many2one('lol.rol',string='Rol Principal')
    fecha = fields.Date(String='Fecha Lanzamiento')
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

    
