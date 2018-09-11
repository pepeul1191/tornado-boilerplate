#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import json
import tornado.web
from main.constants import constants
from main.middlewares import session_false
from main.base import BaseHandler
from main.databases import db_ubicaciones as db
from bson.objectid import ObjectId

class PaisCrear(BaseHandler):
  def post(self):
    rpta = None
    status = 200
    try:
      data = json.loads(self.get_argument('data'))
      ubicaciones = db.ubicaciones
      _id = ubicaciones.insert({
        'nombre': data['nombre'],
        'tipo': 'pais',
      })
      rpta = {
        'tipo_mensaje': 'success',
        'mensaje': [
          'Se ha registrado el pais',
          str(_id)
        ],
      }
    except Exception as e:
      rpta = {
        'tipo_mensaje': 'error',
        'mensaje': [
          'Se ha producido un error en crear el nuevo país',
          str(e)
        ],
      }
      status = 500
    self.set_status(status)
    self.write(json.dumps(rpta))

class PaisEditar(BaseHandler):
  def post(self):
    rpta = None
    status = 200
    try:
      data = json.loads(self.get_argument('data'))
      ubicaciones = db.ubicaciones
      ubicaciones.update_one({
        '_id': ObjectId(data['id']),
      },{
        '$set': {
          'nombre': data['nombre'],
        },
      })
      rpta = {
        'tipo_mensaje': 'success',
        'mensaje': [
          'Se ha editado el pais',
        ],
      }
    except Exception as e:
      rpta = {
        'tipo_mensaje': 'error',
        'mensaje': [
          'Se ha producido un error en editar el país',
          str(e)
        ],
      }
      status = 500
    self.set_status(status)
    self.write(json.dumps(rpta))

class PaisEliminar(BaseHandler):
  def post(self):
    rpta = None
    status = 200
    try:
      data = json.loads(self.get_argument('data'))
      eliminados = data['eliminados']
      if len(eliminados) != 0:
        for id in eliminados:
          ubicaciones = db.ubicaciones
          ubicaciones.delete_one({
            '_id': ObjectId(id),
          })
      rpta = {
        'tipo_mensaje': 'success',
        'mensaje': [
          'Se ha eliminado los paises',
        ],
      }
    except Exception as e:
      e.print_stack
      rpta = {
        'tipo_mensaje': 'error',
        'mensaje': [
          'Se ha producido un error en eliminar los países',
          str(e)
        ],
      }
      status = 500
    self.set_status(status)
    self.write(json.dumps(rpta))
