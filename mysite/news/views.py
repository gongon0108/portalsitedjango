from django.shortcuts import render
from .models import News

# Create your views here.
def news(request):
    news_title_list = News.objects.order_by('created_date')[:5]
    context = {'news_title_list': news_title_list}
    print('news')
    return render(request, 'news/news.html', context)
    #return render(request, 'portal/news.html', {})