# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy

from scrapy.contrib.djangoitem import DjangoItem
from aiwanke.models import GameApp,GameAppScreen

class AppItem(DjangoItem):
    django_model = GameApp
    screen_urls = scrapy.Field()
    game_id = scrapy.Field()

class AppScreenItem(DjangoItem):
    django_model = GameAppScreen

