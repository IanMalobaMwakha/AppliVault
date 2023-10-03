from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name="search"),
    path('job-details/<int:pk>/', views.job_details, name='job_details')
]
