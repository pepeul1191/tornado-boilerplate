#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
from .views import LoginIndex

routes = [
  (r'/login', LoginIndex),
]
