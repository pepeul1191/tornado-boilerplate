#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import tornado
import tornado.template
import os
from tornado.options import define, options

tornado.options.parse_command_line()

path = lambda root,*a: os.path.join(root, *a)

ROOT = os.path.dirname(os.path.abspath(__file__ + "/.."))
MEDIA_ROOT = path(ROOT, 'static')
TEMPLATE_ROOT = path(ROOT, 'templates')

settings = {}
settings['debug'] = True
settings['autoreload'] = True
settings['static_path'] = MEDIA_ROOT
settings['cookie_secret'] = "your-cookie-secret"
settings['xsrf_cookies'] = False
settings['template_loader'] = tornado.template.Loader(TEMPLATE_ROOT)
