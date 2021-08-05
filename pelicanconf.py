#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Lintang JP'
SITENAME = u"LJP's blog"
SITEURL = ''
#THEME = "pelican-themes/plumage"
THEME = "pelican-themes/pelican-sober"
PELICAN_SOBER_ABOUT = "Just an ordinary telecom engineer, working for Online Charging System.."
PELICAN_SOBER_STICKY_SIDEBAR = True
#BOOTSTRAP_THEME = "lovers"
#THEME = "pelican-themes/fresh"
PATH = 'content'
#DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')
TIMEZONE = 'Europe/Dublin'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
STATIC_PATHS = ['images']
# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('My Travelling Logs', 'https://travel.theprasojos.id'),
         ('Firdaus Irlandia', 'https://firdaus.ie'),
         ('Blognya TePot', 'https://vhynaulia.wordpress.com/'),
         ('Theprasojos Family', 'http://theprasojos.wordpress.com'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/jprasojo'),
          ('Linkedin', 'https://www.linkedin.com/in/lintangprasojo'),)

#DEFAULT_PAGINATION = 6
articles_paginator = 6
SITEMAP_SAVE_AS = 'sitemap.xml'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISQUS_SITENAME = "jprasojos"
GOOGLE_ANALYTICS = "UA-56589451-1"

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/index.html'

USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
