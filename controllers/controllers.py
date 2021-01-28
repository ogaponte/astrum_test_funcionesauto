# -*- coding: utf-8 -*-
from odoo import http

# class AstrumTestFuncionesauto(http.Controller):
#     @http.route('/astrum_test_funcionesauto/astrum_test_funcionesauto/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/astrum_test_funcionesauto/astrum_test_funcionesauto/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('astrum_test_funcionesauto.listing', {
#             'root': '/astrum_test_funcionesauto/astrum_test_funcionesauto',
#             'objects': http.request.env['astrum_test_funcionesauto.astrum_test_funcionesauto'].search([]),
#         })

#     @http.route('/astrum_test_funcionesauto/astrum_test_funcionesauto/objects/<model("astrum_test_funcionesauto.astrum_test_funcionesauto"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('astrum_test_funcionesauto.object', {
#             'object': obj
#         })