from django.urls import re_path as url
import menu.views as menu

urlpatterns = [
    url(r'^', menu.index, name='index'),
    url(r'^(\d+)', menu.index, name='index')
]