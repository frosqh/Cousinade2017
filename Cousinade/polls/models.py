# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.

def user_directory_path(instance, filename):
	return settings.MEDIA_ROOT+'/'+instance.author.authorName+'/'+filename

class Author(models.Model):
	authorName = models.CharField(default='anonymous', max_length=200)
	def __str__(self):
		return self.authorName.replace("_"," ")

class Photos(models.Model):
	author = models.ForeignKey(Author)
	photo = models.ImageField(upload_to=user_directory_path)