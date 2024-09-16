from django.urls import path
from home import views

urlpatterns = [
    path('Home/', views.home, name='home'),
]
