from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import RequestContext


def index(request):
	return render(request,'home.html',{'hw':"hello world"}) 