from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('postComment', views.postComment, name="postComment"),
    path('postLike', views.postLike, name="postLike"),
    path('postView', views.postView, name="postView"),
    path('', views.blogHome, name="blogHome"),
    path('<str:slug>', views.blogPost, name="blogPost"),
    path('blogcreate/', views.blogcreate, name="blogcreate"),

]
