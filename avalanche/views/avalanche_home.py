# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def avalanche_home(request):
	return render(request, 'avalanche/map.html', {})