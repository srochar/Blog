#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sebastian Rocha'
SITENAME = u'De todo un Seba'
SITEURL = 'http://alumnos.informatica.utem.cl/~srocha'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('GitGub', 'https://github.com/srochar'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'pelican-cait'

STATIC_PATHS = ['imagenes','Download']

CUSTOM_MENUITEMS = (('Blog', ''),
             ('Quién soy', 'pages/contacto'),)

USE_CUSTOM_MENU = True

CONTACT_EMAIL = "Sebastian.rocha@ceinf.cl"

CONTACTS = (('facebook', 'https://www.facebook.com/sebastian.rochareyes.1'),
            ('twitter', 'https://twitter.com/sebarocha_'),
            ('github','https://github.com/srochar'),
            ('endomondo','http://www.endomondo.com/profile/12168013'),)

DISQUS_SITENAME = "detodounseba"
GOOGLE_ANALYTICS = "UA-45057407-1"

