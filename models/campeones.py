# -*- coding: ISO-8859-1 -*-

from odoo import models, fields, api

class campeones(models.Model):
    _name = 'lol.campeones'

    name = fields.Char(required = True, string='Nombre')
    description = fields.Text(string='Descripción')
    fecha = fields.datetime(required = True)
    idrol = fields.Many2one('lol.rol',string='Rol Principal')

    
