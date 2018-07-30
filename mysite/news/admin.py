from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_date']
    ordering = ['created_date']

# Register your models here.
admin.site.register(News, NewsAdmin)