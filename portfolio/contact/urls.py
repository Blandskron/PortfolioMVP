from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacto_view, name='contacto'),
    path('exito/', views.exito_view, name='exito'),
]