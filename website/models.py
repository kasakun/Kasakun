from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(u'title', max_length=256)
    category = models.CharField(u'category', max_length=80)
    tag = models.CharField(u'tag', max_length=80)
    content = models.TextField(u'content')
    number = models.IntegerField(u'number', default=0)
    introduction = models.TextField(u'introduction')
    pubDate = models.DateTimeField(u'pubDate', default=timezone.now)

    def __str__(self):
        return self.title

    def to_dict(self):
        return dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]])

class ArticleTag(models.Model):
    name = models.CharField(u'name', max_length=256)
    articleId = models.TextField(u'articleId')
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField("title", max_length=256)
    category = models.CharField(u'category', max_length=80)
    fileFormat = models.CharField(u'fileFormat', max_length=10)
    imgUrl = models.CharField("imgUrl", max_length=256)
    number = models.IntegerField(u'number', default=0)
    introduction = models.TextField(u'introduction')
    uploadDate = models.DateTimeField(u'uploadDate', default=timezone.now)
    downloadUrl = models.CharField("downloadUrl", max_length=256)

    def __str__(self):
        return self.title

    def to_dict(self):
        return dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]])

class MediaInstagram(models.Model):
    imgUrl = models.CharField("imgUrl", max_length=256)
    link = models.CharField("link", max_length=256)
    uploadDate = models.DateTimeField(u'uploadDate')

    def to_dict(self):
        return dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]])