#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
from ._distrito import DistritoListar
from ._pais import PaisCrear, PaisEditar, PaisEliminar

routes = [
  (r'/pais/crear', PaisCrear),
  (r'/pais/editar', PaisEditar),
  (r'/pais/eliminar', PaisEliminar),
  (r'/distrito/listar/([a-zA-Z0-9]+)', DistritoListar),
]
