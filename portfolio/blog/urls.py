from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Lista de artículos
    path('<int:post_id>/', views.post_detail, name='post_detail'),  # Detalle del artículo
]
