# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from ..models.activity_db import activity_db
from ..models.locations import locations

def activity(request):
    activity = activity_db.objects.all()
    return render(request, 'avalanche/activity.html', 
        {'activity': activity})


