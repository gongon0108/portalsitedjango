from django.conf.urls import url, include
from django.contrib import admin
from googlecalendar import views

app_name = 'googlecalendar'

urlpatterns = [
    url(r'^', views.calendar, name='calendar'),
]