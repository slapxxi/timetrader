from django.conf.urls import include, url
from django.contrib import admin

import pages.urls
import lists.urls


urlpatterns = [
  url(r'^lists', include(lists.urls)),
  url(r'', include(pages.urls)),
  # url(r'^admin/', include(admin.site.urls)),
]
