from django.urls import path
from . import views

app_name = "userauth"   


urlpatterns = [
    path("register/", views.register_request, name="register")
]


