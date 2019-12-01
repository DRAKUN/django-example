from django.urls import path
from . import views

# app_name = "poll"
urlpatterns = [
    path('', views.home, name='poll_list'),
    path('<int:id>/details/', views.details, name="poll_details"),
]