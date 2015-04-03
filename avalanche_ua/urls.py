from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    #Home
    url(r'^$', 'avalanche.views.avalanche_home.avalanche_home', name='home'),

    #text_report
    url(r'^textreport/$', 'avalanche.views.text_report.text_report', name='textreport'),

    #activity
    url(r'^activity/$', 'avalanche.views.activity.activity', name='activity'),

    url(r'^admin/', include(admin.site.urls)),
)
