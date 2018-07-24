from django.contrib import admin
from .models import Post, News, Profile

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_date']
    ordering = ['created_date']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'content']

admin.site.register(Post)

admin.site.register(News, NewsAdmin)

admin.site.register(Profile, ProfileAdmin)