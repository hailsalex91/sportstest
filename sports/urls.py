from django.conf.urls import patterns, include, url
from roster import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('roster.urls')),
    url(r'^home/$',views.home, name='roster_home'),
    url(r'^WomenGolf/$',views.athleteList, name='roster_athlete_list'),
    url(r'^WomenGolf/(?P<pk>\d+)$',views.athleteView, name='roster_athlete'),
    url(r'^home/coaches(?P<pk>\d+)$',views.coachView, name='roster_coach'),
)