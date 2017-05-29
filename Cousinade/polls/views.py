# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from polls.models import Photos
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

def add(request):
	if request.method == 'POST':
		if ('ajout' in request.POST):
			return render(request, "polls/ajout.html")
		if request.FILES:
			i=0
			for f in request.FILES.getlist('image'):
				i+=1
				m = Photos()
				m.author = request.POST.get('nom')+'_'+request.POST.get('prenom')
				m.photo= f
				m.save()
			return HttpResponseRedirect("view")