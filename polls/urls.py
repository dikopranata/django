from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("room/<str:pk>/",views.room, name="room"),
    path("post/<str:pk>/",views.post,name="post"),
    path("home/",views.home, name="home"),
    path("create-post/",views.createPost, name="create-post"),
    path("update-post/<str:pk>/",views.updatePost, name="update-post"),
    path("delete-post/<str:pk>/",views.deletePost, name="delete-post")
]