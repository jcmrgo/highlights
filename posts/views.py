from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from posts.forms import HighlightForm
from posts.models import *

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required
def index(request):
	highlights = Highlight.objects.filter(user=request.user).order_by('-date_created')
	colores = ["azul", "verde", "rosa","amarillo","celeste","naranja","fiucha","salmon","verde_limon","aqua"]
	return render(request,'home.html',{'highlights':highlights,'colores':colores})

@login_required
def hashtag_highlights(request, hashtag):
	highlights = [h.highlight for h in HighlightHashtag.objects.filter(hashtag__iexact=hashtag, highlight__user=request.user)]
	colores = ["azul", "verde", "rosa","amarillo","celeste","naranja","fiucha","salmon","verde_limon","aqua"]
	return render(request,'home.html',{'highlights':highlights,'colores':colores})

@login_required
def highlights_dashboard(request):
	highlights = Highlight.objects.filter(user=request.user)
	happy = highlights.filter(emotion=1, bigness=5).count()
	sad = highlights.filter(emotion=2, bigness=5).count()
	angry = highlights.filter(emotion=3, bigness=5).count()
	hashtags = HighlightHashtag.objects.filter(highlight__user=request.user)
	hash_highs = []
	for ht in hashtags:
		hash_highs.append([ht.hashtag, HighlightHashtag.objects.filter(hashtag=ht.hashtag, highlight__user=request.user).count()])
	colores = ["azul", "verde", "rosa","amarillo","celeste","naranja","fiucha","salmon","verde_limon","aqua"]
	return render(request,'dashboard.html',{'highlights':highlights,'colores':colores, 'happy':happy,'sad':sad,'angry':angry, 'hash_highs':hash_highs})

@login_required
def public_hashtag_highlights(request, hashtag):
	highlights = [h.highlight for h in HighlightHashtag.objects.filter(hashtag__iexact=hashtag, highlight__share=True)]
	colores = ["azul", "verde", "rosa","amarillo","celeste","naranja","fiucha","salmon","verde_limon","aqua"]
	return render(request,'home.html',{'highlights':highlights,'colores':colores})


@login_required
def highlights_emotions(request, emotion):
	highlights = Highlight.objects.filter(user=request.user, emotion=emotion).order_by('-date_created')
	colores = ["azul", "verde", "rosa","amarillo","celeste","naranja","fiucha","salmon","verde_limon","aqua"]
	return render(request,'home.html',{'highlights':highlights,'colores':colores})

@login_required
def highlights_bigness(request, bigness):
	highlights = Highlight.objects.filter(user=request.user, bigness=bigness).order_by('-date_created')
	colores = ["azul", "verde", "rosa","amarillo","celeste","naranja","fiucha","salmon","verde_limon","aqua"]
	return render(request,'home.html',{'highlights':highlights,'colores':colores})

@login_required
def highlights_public(request):
	highlights = Highlight.objects.filter(share=True).order_by('-date_created')
	colores = ["azul", "verde", "rosa","amarillo","celeste","naranja","fiucha","salmon","verde_limon","aqua"]
	return render(request,'home.html',{'highlights':highlights,'colores':colores})

@login_required
def user_settings(request):
	highlights = Highlight.objects.filter(user=request.user).count()
	return render(request,'settings/settings.html',{'highlights':highlights})


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

