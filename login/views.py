#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
from main.constants import constants
from main.middlewares import session_false
from main.base import BaseHandler
from .helpers import index_css, index_js

class LoginIndex(BaseHandler):
  @session_false
  def get(self):
    locals = {
      'title': 'Bienvenido',
      'mensaje': '',
      'constants': constants,
      'csss': index_css(),
      'jss': index_js(),
    }
    return self.render('login/index.html', locals = locals)
