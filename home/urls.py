#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
from .views import HomeIndex

routes = [
  (r'/', HomeIndex),
]
