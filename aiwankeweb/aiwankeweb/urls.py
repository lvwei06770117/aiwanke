# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aiwankeweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','aiwanke.views.home',name='home'),
    url(r'^aiwanke/', include('aiwanke.urls',namespace='aiwanke')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

#处理游戏图标和封面截图
if settings.DEBUG:
    urlpatterns += patterns("",
        url(r"^media/(?P<path>.*)$", "django.views.static.serve", {"document_root": settings.MEDIA_ROOT}),
    )

