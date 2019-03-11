from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from website.ctrl.article import *
from website.ctrl.book import *
from website.ctrl.instagram import *

import markdown2
import math

tagMap=["primary", "secondary", "success", "danger", "warning", "info", "light", "dark"]
def simpleHash(oldTags):
    newTags = {}
    for oldTag in oldTags:
        newTags[tagMap[hash(oldTag)%len(tagMap)]] = oldTag
    return newTags

# Website entry
def entry(request):
    return render(request, 'entry.html')

# Website home
def home(request):
    return render(request, 'home.html')
# About
def about(request):
    return render(request, 'about.html')

# Blog
def blog(request):
    try:
        page = int(request.GET['page'])
    except:
        page = 1
    
    num = 4

    if page <= 1:
        lastPage = 1
    else:
        lastPage = page - 1
    
    if page == -1:
        page = int(math.ceil(getArticleNum()/4))

    articles = getArticles(page, num)
    recentArticles = getRecentArticles(4)
    tags = getArticleTags()
    tagsAfterHash = simpleHash(tags)

    if len(articles) < num:
        nextPage = page
    else:
        nextPage = page + 1

    # Calculate Pagination
    pages = int(math.ceil(getArticleNum()/4))

    print (pages)

    if page > pages:
        page = 1

    if page < 5:
        pagination = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
    elif page > (pages - 2):
        pagination = {'1': pages - 4, 
                      '2': pages - 3, 
                      '3': pages - 2, 
                      '4': pages - 1, 
                      '5': pages}
    else:
        pagination = {'1': page - 2, 
                      '2': page - 1, 
                      '3': page, 
                      '4': page + 1, 
                      '5': page + 2}

    return render(request, 'blog.html', 
                  {'articles': articles,
                   'recentArticles': recentArticles,
                   'page': page,
                   'lastPage': lastPage,
                   'nextPage': nextPage,
                   'pages': pages,
                   'pagination': pagination,
                    'tags': tagsAfterHash})

def blogByCategory(request):
    try:
        category = request.GET['category']
    except:
        return blog(request)
    try:
        page = int(request.GET['page'])
    except:
        page = 1
    
    num = 4

    if page <= 1:
        lastPage = 1
    else:
        lastPage = page - 1
    
    articles = getArticlesByCategory(page, num, category)
    recentArticles = getRecentArticles(4)
    tags = getArticleTags()
    tagsAfterHash = simpleHash(tags)

    if len(articles) < num:
        nextPage = page
    else:
        nextPage = page + 1

    # Calculate Pagination
    pages = int(math.ceil(getArticleNum()/4))

    if page > pages:
        page = 1

    if page < 5:
        pagination = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
    elif page > (pages - 5):
        pagination = {'1': pages - 4, 
                      '2': pages - 3, 
                      '3': pages - 2, 
                      '4': pages - 1, 
                      '5': pages}
    else:
        pagination = {'1': pages - 2, 
                      '2': pages - 1, 
                      '3': page, 
                      '4': pages + 1, 
                      '5': pages + 2}

    return render(request, 'blogByCategory.html', 
                  {'articles': articles,
                   'recentArticles': recentArticles,
                   'category': category,
                   'page': page,
                   'lastPage': lastPage,
                   'nextPage': nextPage,
                   'pages': pages,
                   'pagination': pagination,
                    'tags': tagsAfterHash})

def blogByTag(request):
    try:
        tag = request.GET['tag']
    except:
        return blog(request)
    try:
        page = int(request.GET['page'])
    except:
        page = 1

    num = 4

    if page <= 1:
        lastPage = 1
    else:
        lastPage = page - 1
    
    articles = getArticlesByTag(page, num, tag)
    recentArticles = getRecentArticles(4)
    tags = getArticleTags()
    tagsAfterHash = simpleHash(tags)

    if len(articles) < num:
        nextPage = page
    else:
        nextPage = page + 1

    # Calculate Pagination
    pages = int(math.ceil(getArticleNum()/4))

    if page > pages:
        page = 1

    if page < 5:
        pagination = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
    elif page > (pages - 5):
        pagination = {'1': pages - 4, 
                      '2': pages - 3, 
                      '3': pages - 2, 
                      '4': pages - 1, 
                      '5': pages}
    else:
        pagination = {'1': pages - 2, 
                      '2': pages - 1, 
                      '3': page, 
                      '4': pages + 1, 
                      '5': pages + 2}

    return render(request, 'blogByTag.html', 
                  {'articles': articles,
                   'recentArticles': recentArticles,
                   'tagName': tag,
                   'page': page,
                   'lastPage': lastPage,
                   'nextPage': nextPage,
                   'pages': pages,
                   'pagination': pagination,
                    'tags': tagsAfterHash})

def article(request):
    try:
        id = request.GET['id']
    except:
        return blog(request)

    backPage = int((getArticleNum() - int(id))/4) + 1
    item = getArticle(id)
    item.number += 1
    item.save()
    articleDict = item.to_dict()
    articleDict['content'] = markdown2.markdown(articleDict['content'],
                                                extras=['fenced-code-blocks', 'tables', 'strike'])
    tags = item.tag.split(',')
    print(tags)
    tagsAfterHash = simpleHash(tags)
    print(tagsAfterHash)

    return render(request, 'article.html',
                  {'article': articleDict,
                   'backPage': backPage,
                   'tags': tagsAfterHash})

def editor(request):
    return render(request, 'editor.html')

def publish(request):
    if request.method == 'POST':
        article = Article()
        article.title = request.POST['formTitle']
        article.category = request.POST['formCategory']
        article.tag = request.POST['formTag']
        article.introduction = request.POST['formIntroduction']
        article.content = request.POST['formContent']
        article.save()

        # save tag
        tags = article.tag.split(',')
        
        for tag in tags:
            if not getArticleTag(tag):
                print(not getArticleTag(tag))
                newTag = ArticleTag()
                newTag.name = tag
                newTag.articleId = str(article.id)
                newTag.save()
            else:
                oldTag = getArticleTag(tag)
                oldTag.articleId = oldTag.articleId + "," + str(article.id)
                oldTag.save()

        return HttpResponseRedirect("/home/blog")
    else:
        return render(request,'editor.html')

# Book
def book(request):
    books = getBooks()
    
    return render(request, 'book.html', 
                  {'books': books})

def demo(request):

    return render(request,'demo.html')

def game(request):

    return render(request,'game.html')

def media(request):
    photos = getPhotos()
    return render(request,'media.html',
                  {'photos': photos})