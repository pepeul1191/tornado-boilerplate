#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
from .views import LoginIndex, LoginAcceder, LoginEstado, LoginSalir

routes = [
  (r'/login', LoginIndex),
  (r'/login/acceder', LoginAcceder),
  (r'/usuario/ver', LoginEstado),
  (r'/usuario/salir', LoginSalir),
]
