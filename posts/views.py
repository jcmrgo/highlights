from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from posts.forms import HighlightForm
from posts.models import Highlight

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required
def index(request):
	highlights = Highlight.objects.filter(user=request.user).order_by('-date_created')
	return render(request,'home.html',{'highlights':highlights})

@login_required
def add_highlight(request):
	h_instance = Highlight(user=request.user)
	if request.method == 'POST':
		form = HighlightForm(request.POST, instance=h_instance)
		if form.is_valid():
			highlight = form.save()
			return HttpResponseRedirect('/')
	else:
		form = HighlightForm(instance=h_instance)
	return render(request,'form.html',{'title':'New Highlight', 'form':form}) 
 