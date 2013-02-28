from django.conf.urls.defaults import patterns, url

from team import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='team_home'),
    url(r'^basketball/$', views.basketballList, name='team_basketball_list'),
    url(r'^basketball/(?P<pk>\d+)$', views.basketball, name='team_basketball'),
    )