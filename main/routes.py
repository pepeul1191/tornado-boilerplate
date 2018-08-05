#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
from login.urls import routes as login_routes
from home.urls import routes as home_routes

routes = []

def load_routes(module_routes):
  for module_route in module_routes:
    routes.append(module_route)

load_routes(login_routes)
load_routes(home_routes)
