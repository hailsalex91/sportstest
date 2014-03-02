__author__ = 'hails'
from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$',views.home, name='roster_home'),
)