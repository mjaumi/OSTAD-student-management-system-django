from django.urls import path
from . import views

# urlpatterns for students app declared here
urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add_student'),
    path('update/<int:student_id>/', views.update, name='update_student'),
]