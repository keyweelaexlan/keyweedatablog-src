#!/usr/bin/env python

# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Alex Lan'
EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')


SITENAME = u'Keywee Data and Algorithms blog'
SITEURL = ''
THEME = '/Users/alex/keywee-new/pelican-themes/pelican-octopress-theme'
PLUGIN_PATH = ['/Users/alex/keywee-new/pelican-plugins']
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook']


PATH = 'content'

NOTEBOOK_DIR = 'notebooks'

TIMEZONE = 'Europe/Paris'

STATIC_PATHS = ['images']

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
