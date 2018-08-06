#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
from main.middlewares import session_true
from main.constants import constants
from main.base import BaseHandler
from .helpers import error_access_css, error_access_js

class ErrorRedirect404(BaseHandler):
  def get(self):
    return self.redirect('/error/access/404')

class Error404(BaseHandler):
  def get(self, numero_error):
    self.set_status(404)
    errores = {
      '404' : {
        'mensaje': 'Archivo no encontrado',
        'numero': '404',
        'descripcion': 'La página que busca no se encuentra en el servidor',
      },
      '505' : {
        'mensaje': 'Acceso restringido',
        'numero': '505',
        'descripcion': 'Necesita estar logueado',
      },
    }
    locals = {
      'title': 'Error',
      'mensaje': '',
      'constants': constants,
      'csss': error_access_css(),
      'jss': error_access_js(),
      'mensaje': errores[str(numero_error)]['mensaje'],
      'numero': errores[str(numero_error)]['numero'],
      'descripcion': errores[str(numero_error)]['descripcion'],
    }
    return self.render('error/access.html', locals = locals)
