#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
from main.middlewares import session_true
from main.constants import constants
from main.base import BaseHandler

class ErrorRedirect404(BaseHandler):
  def get(self):
    return self.redirect('/error/access/404')

class Error404(BaseHandler):
  def get(self):
    self.set_status(404)
    return self.write('error 404')
