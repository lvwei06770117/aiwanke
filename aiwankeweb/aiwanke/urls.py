# -*- coding utf-8 -*-
__author__ = 'wei'

from django.conf.urls import patterns,url
from apps.rest_framework.urlpatterns import format_suffix_patterns
from aiwanke import views

urlpatterns = [
    url(r'^games/$',views.GameAppListView.as_view()),
    #url(r'^games/(?P<source>\d+)-(?P<page>\d+)$',views.GameAppListView.as_view()),
    url(r'^games/(?P<source>\d+)$',views.GameAppListView.as_view()),#='/games/1?page=1'
]
