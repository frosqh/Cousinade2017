# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.

def user_directory_path(instance, filename):
	return settings.MEDIA_ROOT+'/'+instance.author+'/'+filename


class Photos(models.Model):
	author = 'anonymous'
	photo = models.ImageField(upload_to=user_directory_path)