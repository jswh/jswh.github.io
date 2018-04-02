#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_PAGINATION = 15
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%Y/%m/%d %H:%M:%S'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME='Flex'

AUTHOR = 'jswh'
SITENAME = 'Mirror Lake'
SITEURL = 'http://blog.jswh.me'
RELATIVE_URLS = False
SITETITLE = 'Mirror Lake'
SITESUBTITLE = 'stay calm like a mirror lake'
SITELOGO = 'http://cdn.jswh.me/6405755.jpeg'
BROWSER_COLOR = '#333'
DISPLAY_CATEGORIES_ON_MENU = True

FAVICON = 'http://cdn.jswh.me/6405755.jpeg'
ROBOTS = 'index, follow'

COPYRIGHT_YEAR = 2018
CC_LICENSE = { 'name': 'Creative Commons Attribution-ShareAlike', 'version':'4.0', 'slug': 'by-sa' }

MAIN_MENU = True
MAIN_MENU_CATEGORY = True
LINKS = (('个人主页', "http://home.jswh.me"),)

SOCIAL = (('linkedin', 'http://www.linkedin.com/in/曹-维杰-a46255117'),
          ('github', 'https://github.com/jswh'))

CUSTOM_CSS = 'static/custom.css'

GITHUB_CORNER_URL = "https://github.com/jswh/jswh.github.io"
JINJA_ENVIRONMENT = {'extensions': []}
GOOGLE_ANALYTICS = 'UA-58830058-1'
CHANGYAN_APP_ID = 'icytm8uooo'
CHANGYAN_APP_CONF = 'prod_8f0fdacdbce8936c4f8c28f5b8f5b56f'

# Translate
DEFAULT_LANG = 'zh_CN'
OG_LOCALE = 'zh_CN'
LOCALE = 'zh_CN'

# Default theme language.
I18N_TEMPLATES_LANG = 'zh_CN'

# Enable i18n plugin, probably you already have some others here.
PLUGIN_PATHS = ["plugins"]
PLUGINS = ['i18n_subsites']
# Enable Jinja2 i18n extension used to parse translations.
JINJA_EXTENSIONS = ['jinja2.ext.i18n']