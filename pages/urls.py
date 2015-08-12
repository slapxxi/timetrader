from django.conf.urls import url

from pages.views import youtube


urlpatterns = [
  url(r'^youtube/', youtube),
]
