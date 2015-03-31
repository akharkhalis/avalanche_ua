from django.shortcuts import render

def avalanche_home(request):
	return render(request, 'avalanche_home.html', {})