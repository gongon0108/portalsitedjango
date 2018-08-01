from django.conf.urls import url, include
from django.urls import path
from gdiprofile import views

app_name = 'gdiprofile'

urlpatterns = [
    url(r'list', views.profile, name='profile'),
    path(r'detail?id=<int:profile_id>', views.profileDetail, name='detail')
]