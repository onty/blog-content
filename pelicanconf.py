#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Lintang JP'
SITENAME = u"JPrasojo's blog"
SITEURL = ''
#THEME = "pelican-themes/bootstrap"
#THEME = "pelican-themes/Responsive-Pelican"
#THEME = "pelican-themes/pujangga"
THEME = "pelican-themes/fresh"
PATH = 'content'
#DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')
TIMEZONE = 'Europe/Dublin'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
STATIC_PATHS = ['images']
# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Blognya TePot', 'https://vhynaulia.wordpress.com/'),
         ('Theprasojos Family', 'http://theprasojos.wordpress.com'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/jprasojo'),
          ('Linkedin', 'https://www.linkedin.com/in/lintangprasojo'),)

DEFAULT_PAGINATION = 6
#SITEMAP_SAVE_AS = 'sitemap.xml'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
