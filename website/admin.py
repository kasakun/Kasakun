from django.contrib import admin
from .models import Article, ArticleTag, Book, MediaInstagram


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'tag', 'number', 'pubDate', 'introduction',)

class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'articleId',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'number', 'uploadDate', 'introduction',)

class MediaInstagramAdmin(admin.ModelAdmin):
    list_display = ('imgUrl', 'link', 'uploadDate',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleTag, ArticleTagAdmin)
admin.site.register(MediaInstagram, MediaInstagramAdmin)