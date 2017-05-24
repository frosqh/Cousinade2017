# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from polls.models import Photos
from .templates.polls.image import ImageUploadForm

from django.shortcuts import render

# Create your views here.

def index(request):
	if request.method == 'POST':
		if ('ajout' in request.POST):
			return render(request, "polls/ajout.html")
		if request.FILES:
			i=0
			for f in request.FILES.getlist('image'):
				i+=1
				m = Photos()
				m.photo= f
				m.save()
			return HttpResponse("Success :D" + str(i))

	return render(request, "polls/acceuil.html")

def view(request):
	img = Photos.objects.all()
	return render(request, "polls/view.html", {"img" : img})