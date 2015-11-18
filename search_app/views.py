from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

def home(request):
	context = {}
	return render(request, "home.html", context)

def index(request):
    return HttpResponse("Result Index.")

def detail(request, result_id):
    return HttpResponse("You're looking at result %s." % result_id)

def result_show(request, result_id):
    return HttpResponse("You're looking the result: %s page." % result_id)
