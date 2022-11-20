from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('search/', views.search, name="search"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.handleLogin, name="handleLogin"),
    path('logout/', views.handleLogout, name="handleLogout"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="home/passwordreset.html"), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="home/passwordresetdone.html"), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="home/passwordresetconfirm.html"), name="password_reset_confirm"),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="home/passwordresetcomplete.html"), name="password_reset_complete"),
]
