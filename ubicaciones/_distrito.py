#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import datetime
import json
import tornado.web
from main.constants import constants
from main.middlewares import session_false
from main.base import BaseHandler
from main.databases import db_ubicaciones as db
from bson.objectid import ObjectId

class DistritoListar(BaseHandler):
  def get(self, provincia_id):
    ubicaciones = db.ubicaciones
    docs = ubicaciones.find({
      'provincia_id': ObjectId(provincia_id),
    })
    rpta = []
    for doc in docs:
      rpta.append({
        '_id': str(doc['_id']),
        'nombre': doc['nombre']
      })
    rpta = json.dumps(rpta)
    self.write(rpta)
