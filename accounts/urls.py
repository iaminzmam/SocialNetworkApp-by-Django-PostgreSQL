from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_view, name='loginForm'),
    path('signup/', views.register_view, name='registerForm'),
    path('logout/', views.logout_view, name='logoutView'),
    path('', views.profile, name='profileView'),
    path('plans/', views.plansView, name='plansView')

]