from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
   url('home', views.home, name='home'),
   url('about', views.about, name='about'),
   url(r"^delete/(?P<list_id>\d+)", views.delete, name='delete'),
   url(r"^cross_off/(?P<list_id>\d+)", views.cross_off, name='cross_off'),
   url(r"^uncross/(?P<list_id>\d+)", views.uncross, name='uncross'),
   url(r"^edit/(?P<list_id>\d+)", views.edit, name='edit'),
]
