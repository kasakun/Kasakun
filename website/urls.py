from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.entry),
    path('home/', views.home),
    path('home/blog', views.blog),
    path('home/book', views.book),
    path('home/blog/article', views.article),
    path('home/blog/editor', views.editor),
    path('publish/', views.publish)
]