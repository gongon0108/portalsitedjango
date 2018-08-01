from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import logout
from django.contrib.auth import views
from django.contrib.auth.views import logout_then_login
from . import views
from .views import home

app_name = 'portal'

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^calendar/', views.calendar, name='calendar'),
    url(r'^login/', views.login, name='login'),
    #url(r'^logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^logout/', views.logout, name='logout'),
    #url(r'^logout/$', lambda request: logout_then_login(request, "/"), name='logout'),
    url(r'^', views.first_page, name='firstPage'),
    #url(r'^logout2/$', django.contrib.auth.views.logout, {'portal':'logged_out.html'}, name='auth_logout'),

    #url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    #url(r'^auth/', include('social_django.urls', namespace='social')),
]