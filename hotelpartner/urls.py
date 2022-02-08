"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hotelpartner import views
app_name="hotelpartner"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("login", views.login_request, name="login"),
    path("register", views.register_request, name="register"),
    path("logout", views.logout_request, name="logout"),
    path("newhotelchain", views.create_hotel_chain, name="newhotelchain"),
    path("detailhotelchain/<int:pk>-<slug>.html", views.detailhotelchain, name="detailhotelchain"),
    path("detailhotelchain/<int:pk>-<slug>/edit", views.edithotelchain, name="edithotelchain"),
    path("deletehotelchain", views.delete_hotel_chain, name="deletehotelchain"),
    path("hotelchains", views.list_hotel_chain, name="listhotelchains")
]

