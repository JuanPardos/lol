# -*- coding: utf-8 -*-

from datetime import timedelta
from odoo import models, fields, api, exceptions
import time

class rework(models.Model):
    _name = 'lol.rework'

    name = fields.Text()
    idcampeon = fields.Many2one('lol.campeones', String='Campeón')
    fecha = fields.Date(String='Fecha Rework')
    description = fields.Text(string='Descripción')

    start_date = fields.Date(string="Fecha inicio", default=fields.Date.today)
    end_date = fields.Date(string="Fecha final", store=True, compute='_get_end_date', inverse='_set_end_date')
    duration = fields.Float(digits=(6, 2), help="Duration in days", string="Tiempo en el equipo")


    _sql_constraints = [
    ('name_description_check',
        'CHECK(name != description)',
        "La descripción del campeón no puede coincidir con el nombre"),

    ('name_unique',
        'UNIQUE(name)',
        "Ya existe un campeón con ese nombre"),
    ]

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue

            # Add duration to start_date, but: Monday + 5 days = Saturday, so
            # subtract one second to get on Friday instead
            duration = timedelta(days=r.duration, seconds=-1)
            r.end_date = r.start_date + duration

    def _set_end_date(self):
        for r in self:
            if not (r.start_date and r.end_date):
                continue

            # Compute the difference between dates, but: Friday - Monday = 4 days,
            # so add one day to get 5 days instead
            r.duration = (r.end_date - r.start_date).days + 1
  
 

    
