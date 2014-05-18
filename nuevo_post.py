#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import dateutil.parser
import datetime
import os
from slugify import slugify

def new_post(titulo, fecha = None):
    if fecha is None:
        fecha = datetime.datetime.now() # Fecha/tiempo actual
    else:
        fecha = dateutil.parser.parse(fecha) # Trata de parsear la fecha, probablemente deba capturar la excepcion
    template = '''title: {titulo}\ncategory: misc\ntags: '''
    
    slug = titulo.replace(' ','-') # Hacemos un slug, reemplaza espacios, caracteres extraños y demases
    stamp_fichero = fecha.strftime('%Y-%m-%d') # año/mes/dia
    
    fichero = '{fecha}-{titulo}.{ext}'.format(fecha = stamp_fichero, titulo = slug, ext = 'md')
    fichero = os.path.join(os.getcwd(), 'content', fichero)

    carpeta_imagenes = '{titulo}'.format(titulo = slug)
    carpeta_imagenes = os.path.join(os.getcwd(),'content','imagenes',carpeta_imagenes)

    print(fichero)
    
    if os.path.exists(fichero):
        print('El fichero', fichero, 'ya existe! intentelo de nuevo!')
    else:
        os.mkdir(carpeta_imagenes)
        with open(fichero, 'w') as f:
            f.write(template.format(titulo = titulo))
        print('Se creo el nuevo post', fichero)


title = raw_input('Titulo del post: ')
new_post(title);
