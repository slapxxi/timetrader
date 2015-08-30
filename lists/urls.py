from django.conf.urls import url

from . import views


urlpatterns = [
  url(r'unique/$', views.show, name='view_list'),
  url(r'new/$', views.new, name='new_list'),
  url(r'^/$', views.index),
]
