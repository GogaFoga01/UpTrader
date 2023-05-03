from django.urls import re_path as url
from django.urls import path
from django.urls import include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('menu.urls')),
]
