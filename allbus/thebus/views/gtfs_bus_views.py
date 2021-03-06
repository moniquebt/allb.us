#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from django.conf import settings
from django.http import HttpResponse

import json
from ..utilities.thebus.client import parse_xml_to_dict
from ..utilities.thebus.client import TheBusClient
from ..utilities.time.utilities import naive_to_timestamp


def bus_details(request, bus):
    c = TheBusClient(settings.THEBUS_API_CLIENT_TOKEN)
    v_json = c.track_vehicle(int(bus), parse_xml_to_dict)
    vehicles = v_json.get('vehicles', None)
    vehicle = vehicles.get('vehicle', None)

    if 'last_message' in vehicle:
        naive_datetime = datetime.datetime.strptime(
            vehicle['last_message'],
            "%m/%d/%Y %I:%M:%S %p")
        vehicle['last_message_ts'] = naive_to_timestamp(
            naive_datetime, tz='Pacific/Honolulu')

    return HttpResponse(json.dumps(vehicle), mimetype="application/json")

# vim: filetype=python
