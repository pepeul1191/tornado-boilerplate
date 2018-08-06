#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
from main.middlewares import session_true
from main.constants import constants
from main.base import BaseHandler

class HomeIndex(BaseHandler):
  @session_true
  def get(self):
    return self.write('home')
