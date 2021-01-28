# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime
from datetime import date
import logging
_logger = logging.getLogger(__name__)

class HPresupuestoConfig(models.Model):
    _name = 'historico.presupuesto.config'

    name = fields.Integer(string="Año")
    borrado_primer_trimestre = fields.Date(help="El primer día del primer trimestre")
    borrado_segundo_trimestre = fields.Date(help="El primer dia del segundo trimestre")
    borrado_tercer_trimestre = fields.Date(help="El primer dia del tercer trimestre")
    borrado_cuarto_trimestre = fields.Date(help="El primer dia del cuarto trimestre")

    def borrado_almacenado_presupuesto(self):
      _logger.info('----------- borrado_almacenado_presupuesto() -------------')
      hoy = date.today()
      if self.borrado_primer_trimestre == hoy:
        _logger.info('SI ES HOY!!! GUARDA EN HISTORICO Y BORRA !!!')
      else:
        _logger.info('No haré nada')
                  

#Gurdar datos en modelo:
# class HistoricoPresupuesto(models.Model):
#     _name = 'historico.presupuesto'

    
