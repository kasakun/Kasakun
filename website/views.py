from django.shortcuts import render
from django.http import HttpResponse

from website.ctrl.article import *
from website.ctrl.book import *

# Website entry
def entry(request):
    return render(request, 'entry.html')

# Website home
def home(request):
    return render(request, 'home.html')

# Blog
def blog(request):
    try:
        page = int(request.GET['page'])
        num = int(request.GET['num'])
    except:
        page = 1
        num = 4

    if page <= 1:
        lastPage = 1
    else:
        lastPage = page + 1
    
    articles = getArticles(page, num)
    categories = getArticleCategories()
    recentArticles = getRecentArticles(4)

    if len(articles) < num:
        nextPage = page
    else:
        nextPage = page + 1
    

    return render(request, 'blog.html', 
                  {'articles': articles,
                   'categories': categories,
                   'recentArticles': recentArticles,
                   'lastPage': lastPage,
                   'nextPage': nextPage})

# Book
def book(request):
    try:
        page = int(request.GET['page'])
        num = int(request.GET['num'])
    except:
        page = 1
        num = 4

    if page <= 1:
        lastPage = 1
    else:
        lastPage = page + 1
    
    books = getArticles(page, num)
    recentBooks = getRecentBooks(4)

    if len(books) < num:
        nextPage = page
    else:
        nextPage = page + 1
    

    return render(request, 'book.html', 
                  {'books': books,
                   'recentBooks': recentBooks,
                   'lastPage': lastPage,
                   'nextPage': nextPage})