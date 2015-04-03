# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from ..models import activity_db

def activity(request):
    activity_db = activity_db.objects.all()
    return render(request, 'avalanche/activity.html', 
        {'activity_db': activity_db})


