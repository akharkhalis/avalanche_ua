# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def text_report(request):
	return render(request, 'avalanche/text.html', {})