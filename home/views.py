#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
from main.constants import constants
from main.base import BaseHandler

class HomeIndex(BaseHandler):
  def get(self):
    return self.write('home')
