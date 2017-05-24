from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
	url(r'^$', views.index, name='acceuil'),
	url(r'^view$', views.view, name='view'),
	url(r'^ajout$', views.index, name='ajout'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)