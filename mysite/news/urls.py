from django.conf.urls import url, include
from django.contrib import admin
from news import views
from django.urls import path

app_name = 'news'

urlpatterns = [
    url(r'^', views.news, name='news')
]