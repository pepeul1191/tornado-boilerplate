#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
from .views import Error404

routes = [
  (r'/error/access/404', Error404),
]
