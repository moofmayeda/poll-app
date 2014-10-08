from django.conf.urls import patterns, url

from todos import views

urlpatterns = patterns('',
  url(r'^$', views.IndexView.as_view(), name='index'),
  url(r'^update/$', views.update_completed, name='update_completed'),
)
