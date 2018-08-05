#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import tornado.httpserver
from main.settings import settings
from main.routes import routes

def main():
  application = tornado.web.Application(routes, **settings)
  http_server = tornado.httpserver.HTTPServer(application)
  #options.port  = int(raw_input('Ingrese el puerto:'))
  #http_server.listen(options.port)
  #print "Instancia del servidor Tornado ejecutándose en el puerto : " + str(options.port)
  http_server.listen(8888)
  tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
  main()
