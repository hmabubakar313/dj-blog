from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create/', views.create, name='create'),
    path('save_post/', views.save_post, name='save_post'),
    path('feed/', views.feed, name='feed'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
