from django.shortcuts import render
from django.http import HttpResponse
from .models import Exercise

def index(request):
	# return HttpResponse("Fitness app index :)")
	return HttpResponse(Exercise.objects.all())
