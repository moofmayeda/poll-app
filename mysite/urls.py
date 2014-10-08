from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^todos/', include('todos.urls', namespace="todos")),
    url(r'^admin/', include(admin.site.urls)),
)
