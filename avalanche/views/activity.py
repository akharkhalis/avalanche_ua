# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def activity(request):
	return render(request, 'avalanche/activity.html', {})