from django.conf.urls import url, include
from django.contrib import admin
from credo import views

app_name = 'credo'

urlpatterns = [
    url(r'^', views.credo, name='credo'),
]