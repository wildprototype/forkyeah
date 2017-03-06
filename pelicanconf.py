#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jared Nielsen'
SITENAME = u'Fork Yeah!'
#SITEURL = 'http://forkyeah.io'
GITHUB_URL = 'https://github.com/wildprototype/forkyeah'
GOOGLE_ANALYTICS = ''
TWITTER_USERNAME = 'jarednielsen'


PATH = 'content'
STATIC_PATHS = ['images', 'files', 'extra/robots.txt', 'extra/favicon.ico', 'static/custom.css']
CUSTOM_CSS = 'static/custom.css'

ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}/index.html'
INDEX_SAVE_AS = 'recipes.html'
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [
    ('Recipes', '/recipes.html')
]
USE_FOLDER_AS_CATEGORY = True

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
#SOCIAL_WIDGET_NAME = ''
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DISPLAY_TAGS_ON_SIDEBAR = True

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
