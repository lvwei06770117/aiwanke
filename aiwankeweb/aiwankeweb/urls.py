from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aiwankeweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','aiwanke.views.home',name='home'),
    url(r'^aiwanke/', include('aiwanke.urls',namespace='aiwanke')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns +=  static(settings.STATIC_URL)

