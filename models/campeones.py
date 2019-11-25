# -*- coding: ISO-8859-1 -*-

from odoo import models, fields, api

class campeones(models.Model):
    _name = 'lol.campeones'

    name = fields.Char(required = True, string='Nombre')
    description = fields.Text(string='Descripción')
    fecha = fields.Char(required=True,string='Fecha Lanzamiento')
    idrol = fields.Many2one('lol.rol',string='Rol Principal')

    
