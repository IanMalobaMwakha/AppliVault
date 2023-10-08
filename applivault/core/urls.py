from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name="search"),
    path('job-details/<int:pk>/', views.job_details, name='job_details'),
    path('saved-jobs/', views.saved_jobs, name='saved_jobs'),
    path('applied-jobs/', views.applied_jobs, name='applied_jobs'),
    path('post-a-job/', views.post_job, name='post_job'),
    path('my-posted-jobs/', views.my_posted_jobs, name='my_posted_jobs'),


]
