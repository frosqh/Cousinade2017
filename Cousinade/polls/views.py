# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from polls.models import Photos, Author
from .templates.polls.image import ImageUploadForm

from django.shortcuts import render

# Create your views here.

def index(request):
	if request.method=='POST':
		return add(request)
	return render(request, "polls/acceuil.html")

def view(request):
	if request.method=='POST':
		return add(request)
	img = Photos.objects.all()
	return render(request, "polls/view.html", {"img" : img})

def viewhome(request):
	if request.method=='POST':
		if ('all' in request.POST):
			return HttpResponseRedirect('view')
		if ('sort' in request.POST):
			return HttpResponseRedirect('choice')

	return render(request, "polls/viewhome.html")

def add(request):
	if request.method == 'POST':
		if ('ajout' in request.POST):
			return render(request, "polls/ajout.html")
		if ('view' in request.POST):
			return HttpResponseRedirect("viewhome")
		if request.FILES:
			i=0
			for f in request.FILES.getlist('image'):
				author = request.POST.get('nom')+'_'+request.POST.get('prenom')
				i+=1
				l = Author.objects.all().filter(authorName=author)
				if l.count() == 0:
					a = Author()
					a.authorName = request.POST.get('nom')+'_'+request.POST.get('prenom')
					a.save()
				else:
					a = l[0]
				m = Photos()
				m.author = a
				m.photo= f
				m.save()
			return HttpResponseRedirect("view")

def choice(request):
	return render(request, "polls/authorChoice.html", {"authors" : Author.objects.all().order_by("authorName")})