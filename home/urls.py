from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('contact/', views.contact),
    path('home/', views.home),
    path('email/', views.email),
    path('success/', views.success),
    path('projects/', views.projects),
    path('analytics/', views.analytics),

]