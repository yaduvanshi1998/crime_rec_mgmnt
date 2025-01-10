"""
URL configuration for crime_rec_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from crime_rec_app import views


urlpatterns = [
    path("", views.login, name='redirectlogin'),
    path("login", views.login, name='login'),
    path("base", views.base, name='base'),
    path("signup", views.signup, name='signup'),
    path("addCourt", views.add_court, name ='addCourt'),
    path("addJudge", views.add_judge, name='addJudge'),
    path("addVictim", views.add_victim, name='addVictim'),
    path("addOffender", views.add_offender, name='addOffender'),
    path("addCrime", views.add_crime, name='addCrime'),
    path("addPrison", views.add_prison, name='addPrison'),
    path("addGuard", views.add_guard, name='addGuard'),

]

'''
Run this commands to add the remote link & fetch all the branches
git remote add origin https://github.com/yaduvanshi1998/crime_rec_mgmnt.git
git fetch --all

'''