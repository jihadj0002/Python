from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.user, name="user"),
    path("login/", views.login, name="login"),
    path("reg", views.reg, name="reg")
    
]
