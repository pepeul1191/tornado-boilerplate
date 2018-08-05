#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
from main.constants import constants
from main.base import BaseHandler
from .helpers import index_css, index_js

class LoginIndex(BaseHandler):
  def get(self):
    locals = {
      'constants': constants,
      'title': 'Bienvenido',
      'csss': index_css(),
      'jss': index_js(),
    }
    return self.render('login/index.html', locals = locals)
