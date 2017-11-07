#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('home', "http://home.jswh.me"),)

DEFAULT_PAGINATION = 15

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME='Flex'

AUTHOR = 'jswh'
SITENAME = 'Mirror Lake'
SITEURL = 'https://blog.jswh.me'
RELATIVE_URLS = False
SITETITLE = 'Mirror Lake'
SITESUBTITLE = 'stay calm like a mirror lake......'
SITELOGO = 'http://cdn.jswh.me/6405755.jpeg'
BROWSER_COLOR = '#333'

FAVICON = 'http://cdn.jswh.me/6405755.jpeg'
ROBOTS = 'index, follow'

COPYRIGHT_YEAR = 2018
CC_LICENSE = { 'name': 'Creative Commons Attribution-ShareAlike', 'version':'4.0', 'slug': 'by-sa' }

EXTRA_PATH_METADATA = {
}
#CUSTOM_CSS = 'static/custom.css'

MAIN_MENU = True

SOCIAL = (('linkedin', 'http://www.linkedin.com/in/曹-维杰-a46255117'),
          ('github', 'https://github.com/jswh'))

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html')
            )

GITHUB_CORNER_URL = "https://github.com/jswh/jswh.github.io"
JINJA_ENVIRONMENT = {'extensions': []}
GOOGLE_ANALYTICS = 'UA-58830058-1'
