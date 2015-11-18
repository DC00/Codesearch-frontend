from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search_app/', include('search_app.urls')),

    url(r'^$', 'search_app.views.home', name='home'),
]
