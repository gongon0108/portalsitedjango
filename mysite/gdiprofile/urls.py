from django.conf.urls import url, include
from django.urls import path
from gdiprofile import views

app_name = 'gdiprofile'

urlpatterns = [
    url(r'list', views.profile, name='profile'),
    #url(r'detail(?P<slug>[-\w]+)/$', views.profileDetail, name='detail')
    #url(r'detail?.+', views.profileDetail, name='detail')
    #path('detail/<int:profile_name>/', views.profileDetail, name='detail')
    path(r'detail?id=<int:profile_id>', views.profileDetail, name='detail')
    #url(r'^detail?.+$', views.profileDetail, name='detail')
]