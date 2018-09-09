#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
from ._distrito import DistritoListar

routes = [
  (r'/distrito/listar/([a-zA-Z0-9]+)', DistritoListar),
]
