# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.

class Photos(models.Model):
	photo = models.ImageField(upload_to=settings.MEDIA_ROOT)