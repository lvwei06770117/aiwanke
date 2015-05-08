# -*- coding: utf-8 -*-

# Scrapy settings for aiwankecrawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
AIWANKE_DIR = os.path.join(BASE_DIR, os.pardir)
IMAGES_STORE = os.path.join(AIWANKE_DIR,'aiwankeweb/media')

BOT_NAME = 'aiwankecrawl'

SPIDER_MODULES = ['aiwankecrawl.spiders']
NEWSPIDER_MODULE = 'aiwankecrawl.spiders'

ITEM_PIPELINES = {
    'aiwankecrawl.pipelines.IconImagesPipeline': 100,
    'aiwankecrawl.pipelines.DjangoPipeline': 200,
    'aiwankecrawl.pipelines.ScreenImagesPipeline': 300,
    #'aiwankecrawl.pipelines.JsonWriterPipeline': 400,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'aiwankecrawl (+http://www.yourdomain.com)'

# Setting up django's project full path.
import sys
sys.path.insert(0,os.path.join(AIWANKE_DIR,'aiwankeweb'))
# Setting up django's settings module name.
# This module is located at aiwanke/aiwankeweb/aiwankeweb/settings.py.
os.environ['DJANGO_SETTINGS_MODULE'] = 'aiwankeweb.settings'

#fire up django settings modules
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
try:
    settings.INSTALLED_APPS
except ImproperlyConfigured as exc:
    pass
#settings._setup()
import django
if settings.configured:
    django.setup()

