from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('projects/', views.projects, name='projects'),
    path('equipment/', views.equipment, name='equipment'),
    path('equipment/<int:equipment_id>/', views.equipment_detail, name='equipment_detail'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('documents/', views.documents, name='documents'),
    path('documents/download/<int:document_id>/', views.download_document, name='download_document'),
]

