#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import datetime
import json
import tornado.web
from main.constants import constants
from main.middlewares import session_false
from main.base import BaseHandler
from .helpers import index_css, index_js

class LoginIndex(BaseHandler):
  @session_false
  def get(self):
    locals = {
      'title': 'Bienvenido',
      'mensaje': '',
      'constants': constants,
      'csss': index_css(),
      'jss': index_js(),
    }
    return self.render('login/index.html', locals = locals)

class LoginAcceder(BaseHandler):
  def post(self):
    mensaje = ''
    continuar = True
    try:
      usuario = self.get_argument('usuario')
      # validar usuario/sistema
      r1 = requests.post(
        constants['servicios']['accesos']['url'] + 'sistema/usuario/validar',
        headers = {
          constants['servicios']['accesos']['key'] : constants['servicios']['accesos']['secret'],
        },
        data = {
          'usuario' : usuario,
          'sistema_id' : constants['sistema_id'],
        }
      )
      if r1.status_code == 200:
        if r1.text != '1':
          continuar = False
          mensaje = 'Usuario no se encuentra registrado en el sistema'
      else:
        continuar = False
        mensaje = 'Se ha producido un error no esperado al validar usuario/sistema'
    except ConnectionError as e:
      rpta = {
        'tipo_mensaje': 'error',
        'mensaje': [
          'No se puede acceder al servicio de validación de usuario/sistema',
          str(e)
        ],
      }
      print(rpta)
      mensaje = rpta['mensaje'][0]
      continuar = False
    except Exception as e:
      rpta = {
        'tipo_mensaje': 'error',
        'mensaje': [
          'Se ha producido un error no controlado al validar usuario/sistema',
          str(e)
        ],
      }
      print(rpta)
      mensaje = rpta['mensaje'][0]
      continuar = False
    # validar usuario/contrasenia
    if continuar == True:
      try:
        usuario = self.get_argument('usuario')
        contrasenia = self.get_argument('contrasenia')
        # validar usuario/sistema
        r2 = requests.post(
          constants['servicios']['accesos']['url'] + 'usuario/externo/validar',
          headers = {
            constants['servicios']['accesos']['key'] : constants['servicios']['accesos']['secret'],
          },
          data = {
            'usuario' : usuario,
            'contrasenia' : contrasenia,
          }
        )
        if r2.status_code == 200:
          if r2.text != '1':
            continuar = False
            mensaje = 'Usuario y/o contraseña no coincide'
          else:
            # habilitar session
            self.set_secure_cookie('usuario', usuario)
            self.set_secure_cookie('estado', 'activo')
            self.set_secure_cookie('tiempo', str(datetime.datetime.now()))
            self.redirect('/')
        else:
          continuar = False
          mensaje = 'Se ha producido un error no esperado al validar usuario/contraseña'
      except ConnectionError as e:
        rpta = {
          'tipo_mensaje': 'error',
          'mensaje': [
            'No se puede acceder al servicio de validación de usuario/contrasenia',
            str(e)
          ],
        }
        print(rpta)
        mensaje = rpta['mensaje'][0]
        continuar = False
      except Exception as e:
        rpta = {
          'tipo_mensaje': 'error',
          'mensaje': [
            'Se ha producido un error no controlado al validar usuario/contrasenia',
            str(e)
          ],
        }
        print(rpta)
        mensaje = rpta['mensaje'][0]
        continuar = False
    locals = {
      'title': 'Login',
      'mensaje': mensaje,
      'constants': constants,
      'csss': index_css(),
      'jss': index_js(),
    }
    self.set_status(500)
    return self.render('login/index.html', locals = locals)

class LoginEstado(BaseHandler):
  def get(self):
    rpta = ''
    if not self.get_secure_cookie('usuario'):
      rpta = '<h1>El usuario no se encuentra logueado</h1>'
    else:
      rpta = '<h1>Usuario Logeado</h1><ul><li>' + str(self.get_secure_cookie('usuario').decode("utf-8")) + '</li><li>' +  str(self.get_secure_cookie('tiempo').decode("utf-8")) + '</li><li>' + str(self.get_secure_cookie('estado').decode("utf-8")) + '</li></ul>'
    self.write(rpta)

class LoginSalir(BaseHandler):
  def get(self):
    if self.get_secure_cookie('usuario'):
      self.clear_cookie('usuario')
    if self.get_secure_cookie('tiempo'):
      self.clear_cookie('tiempo')
    if self.get_secure_cookie('estado'):
      self.clear_cookie('estado')
    self.redirect('/login')
    return
