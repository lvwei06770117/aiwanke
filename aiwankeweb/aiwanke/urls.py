# -*- coding: utf-8 -*-
__author__ = 'wei'

from django.conf.urls import patterns,url
from django.conf.urls.static import static
from django.conf import settings
from apps.rest_framework.urlpatterns import format_suffix_patterns
from aiwanke import views

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]

#picture of game app,use static serving ,change to nginx proxy when deployed.
#urlpatterns +=static(settings.GAME_PICTURE_URL, document_root=settings.GAME_PICTURE_ROOT)

#rest api
urlpatterns += [
    url(r'^api/$',views.GameAppListView.as_view()),
    #url(r'^games/(?P<source>\d+)-(?P<page>\d+)$',views.GameAppListView.as_view()),
    url(r'^api/(?P<source>\d+)$',views.GameAppListView.as_view()),#='/games/1?page=1'
]
