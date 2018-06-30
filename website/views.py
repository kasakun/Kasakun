from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from website.ctrl.article import *
from website.ctrl.book import *

import markdown2

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
        # num = int(request.GET['num'])
    except:
        page = 1
    
    num = 4
    
    if page <= 1:
        lastPage = 1
    else:
        lastPage = page - 1
    
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

def article(request):
    try:
        id = request.GET['id']
    except:
        return blog(request)

    backPage = int((getArticleNum() - int(id))/4) + 1
    item = getArticle(id)
    articleDict = item.to_dict()
    articleDict['content'] = markdown2.markdown(articleDict['content'])
    return render(request, 'article.html',
                  {'article': articleDict,
                   'backPage': backPage})

def editor(request):
    # try:
    #     article_id = request.GET['articleid']
    # except:
    #     return articles(request)
    # logging_status = get_logging_status(request)
    # item = get_article(article_id)
    # article_dict = item.to_dict()
    # article_dict['categorys'] = article_dict['category'].split(',')
    return render(request, 'editor.html')

def publish(request):
    if request.method == 'POST':
        article = Article()
        article.title = request.POST['formTitle']
        article.category = request.POST['formCategory']
        article.introduction = request.POST['formIntroduction']
        article.content = request.POST['formContent']
        article.save()
        print(request.POST['formTitle'])
        return HttpResponseRedirect("/home/blog")
    else:
        return render(request,'editor.html')

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
        lastPage = page - 1
    
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