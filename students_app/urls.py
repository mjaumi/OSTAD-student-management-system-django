from django.urls import path
from . import views

# urlpatterns for students app declared here
urlpatterns = [
    path('', views.home, name='home')
]