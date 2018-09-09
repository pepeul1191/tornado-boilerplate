#!/usr/bin/env python
# -*- coding: utf-8 -*-
from login.urls import routes as login_routes
from home.urls import routes as home_routes
from error.urls import routes as error_routes
from ubicaciones.urls import routes as ubicaciones_routes

routes = []

def load_routes(module_routes):
  for module_route in module_routes:
    routes.append(module_route)

load_routes(login_routes)
load_routes(home_routes)
load_routes(error_routes)
load_routes(ubicaciones_routes)
