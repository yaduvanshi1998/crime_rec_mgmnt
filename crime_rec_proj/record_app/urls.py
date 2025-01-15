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
from django.urls import path
from record_app import views


urlpatterns = [
    path("court", views.court_record, name = 'court_record'),
    path("judge", views.judge_record, name = 'judge_record'),
    path("victim", views.victim_record, name = 'victim_record'),
    path("offender", views.offender_record, name = 'offender_record'),
    path("crime", views.crime_record, name = 'crime_record'),
    path("prison", views.prison_record, name = 'prison_record'),
    path("guard", views.guard_record, name = 'guard_record'),
    path("punishment", views.punishment_record, name = 'punishment_record'),
]

'''
Run this commands to add the remote link & fetch all the branches
git remote add origin https://github.com/yaduvanshi1998/crime_rec_mgmnt.git
git fetch --all

'''