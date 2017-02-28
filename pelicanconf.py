#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jared Nielsen'
SITENAME = u'Fork Yeah'
SITEURL = ''

PATH = 'content'

CUSTOM_CSS = 'static/custom.css'

STATIC_PATHS = ['images', 'files', 'extra/robots.txt', 'extra/favicon.ico', 'static/custom.css']

ARTICLE_URL = '{slug}'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs'

THEME = 'pelican-themes/pelican-bootstrap3/'
BOOTSTRAP_THEME = 'readable'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['assets', 'sitemap', 'gravatar','i18n_subsites', 'tag_cloud']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

HIDE_SIDEBAR = True
# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DISPLAY_TAGS_ON_SIDEBAR = True

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
