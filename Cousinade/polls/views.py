# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from polls.models import Photos, Author
from .templates.polls.image import ImageUploadForm
from wsgiref.util import FileWrapper
from django.shortcuts import render
import zipfile
import os
from os.path import basename


# Create your views here.

def index(request):
	if request.method=='POST':
		return add(request)
	return render(request, "polls/acceuil.html")

def view(request):
	if request.method=='POST':
		return add(request)
	img = Photos.objects.all()
	request.session['sort'] = None
	return render(request, "polls/view.html", {"img" : img})

def viewhome(request):
	if request.method=='POST':
		if ('all' in request.POST):
			return HttpResponseRedirect('view')
		if ('sort' in request.POST):
			return HttpResponseRedirect('choice')

	return render(request, "polls/viewHome.html")

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
	if request.method == 'POST':
		if 'author' in request.POST:
			author = request.POST.get('author').replace(" ","_")
			l = Author.objects.all().filter(authorName=author)
			request.session['sort'] = author
			return render(request, "polls/view.html", {"img" : Photos.objects.all().filter(author = l[0])})
	return render(request, "polls/authorChoice.html", {"authors" : Author.objects.all().order_by("authorName")})

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

def test(request):
	zip = zipfile.ZipFile('compfiles.zip', 'w')
	if request.session['sort'] != None:
		m = Author.objects.all().filter(authorName=request.session['sort'])
		l =Photos.objects.all().filter(author = m[0])
	else:
		l = Photos.objects.all()
	with cd(os.path.abspath(os.path.join(os.getcwd(), os.pardir))):
		for n in l:
			zip.write(os.getcwd()+n.photo.url, basename(os.getcwd()+n.photo.url))
		zip.close()
	with open('compfiles.zip', 'rb') as pdf:
		response = HttpResponse(pdf.read())
		response['content_type'] = 'application/zip'
		if request.session['sort'] != None:
			response['Content-Disposition'] = 'attachment;filename=photos_'+request.session['sort']+'.zip'
		else:
			response['Content-Disposition'] = 'attachment;filename=photos_all.zip'
		return response