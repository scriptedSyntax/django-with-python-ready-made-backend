from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # /genre/
    path('', views.IndexView.as_view(), name="index"),

    # /genre/1
    path('<int:pk>/', views.DetailsView.as_view(), name="details"),

    # /genre/register/
    path('register/', views.UserFormView.as_view(), name="register"),
]
