from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aiwankeweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','aiwanke.views.home',name='home'),
    url(r'^', include('aiwanke.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
