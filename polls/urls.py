from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("room/<str:pk>/",views.room, name="room"),
    path("home/",views.home, name="home")
]