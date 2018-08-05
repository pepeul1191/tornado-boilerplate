import tornado.web
import sys
import logging

logger = logging.getLogger('boilerplate.' + __name__)

class BaseHandler(tornado.web.RequestHandler):
  def set_default_headers(self):
    self.set_header('Content-type', 'text/html; charset=UTF-8')
    self.set_header('Server', 'TornadoServer/4.5.1; Ubuntu; Python')

  def get_request():
    return self
