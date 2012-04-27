from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required
def index(request):
	return render(request,'home.html',{'hw':"hello world"})