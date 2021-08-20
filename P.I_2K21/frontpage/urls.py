from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test", views.login, name="login"),
    path("<str:not_found>", views.notfound, name="notfound")
]