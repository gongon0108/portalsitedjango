from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Profile

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'portal/login.html')

def post_list(request):
    return render(request, 'portal/home.html', {})

def news(request):
    news_title_list = News.objects.order_by('created_date')[:5]
    context = {'news_title_list': news_title_list}
    return render(request, 'portal/news.html', context)
    #return render(request, 'portal/news.html', {})

def calendar(request):
    return render(request, 'portal/calendar.html')

def profile(request):
    profile_list = Profile.objects.order_by('name')
    context = {'profile_list': profile_list}
    return render(request, 'portal/profile.html', context)

def credo(request):
    return render(request, 'portal/credo.html')



