from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from . import views
from .views import home


urlpatterns = [
    url(r'^$', views.post_list, name='home'),
    url(r'^news/', views.news, name='news'),
    url(r'^login/', views.login, name='login'),
    url(r'^calendar/', views.calendar, name='calendar'),
    url(r'^credo/', views.credo, name='credo'),
    #url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url(r'profile/', views.profile, name='profile')
    #url(r'^$', home , name='home'),
    #url(r'^logout/$', views.logout, name='logout'),
]