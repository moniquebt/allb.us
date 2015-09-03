#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import www_views
from .views import stop_views
from .views import bus_views
from .views import route_views


urlpatterns = [
    # www related views
    url(r'^$', www_views.slash, name="slash"),
    url(r'^placard/$', www_views.placard, name="placard"),
    url(r'^up/$', www_views.about, name="about"),

    # route related views
    url(r'^routes/(?P<route>[a-zA-Z0-9]+)/(?P<direction>(west|east))/$',
        route_views.route_map, name="route_map"),

    # stop related views
    url(r'^stops/$', stop_views.stop_search, name="stop_search"),
    url(r'^es/$', stop_views.stop_near, name="stop_near"),
    url(r'^es/near/(?P<latitude>[\-\.0-9]+)/(?P<longitude>[\-\.0-9]+)/$',
        stop_views.stop_nearby, name="stop_nearby"),

    url(r'^(?P<stop>\d+)/$', stop_views.stop_details, {'route': None},
        name="stop_details_no_route"),
    url(r'^(?P<stop>\d+)/map/$', stop_views.stop_map, name="stop_maps"),
    url(r'^(?P<stop>\d+):(?P<route>[a-zA-Z0-9]+)/bus/(?P<bus>\d+)/(?P<direction>(west|east))/$', stop_views.stop_bus_map, name="stop_bus_map"),

    url(r'^(?P<stop>\d+):(?P<route>[a-zA-Z0-9]+)/$', stop_views.stop_details,
        name="stop_details"),

    # bus related views
    url(r'^buses/(?P<bus>[\d]+).json$', bus_views.bus_details, name="bus_details"),
]

# vim: filetype=python
