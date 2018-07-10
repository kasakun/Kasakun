from website.models import Article
from website.models import ArticleTag
from website.models import Book
from django.utils import timezone

def getArticles(page, num):
    items = Article.objects.order_by('-pubDate').all()[(page - 1) * num: page * num]
    result = []
    for item in items:
        print(item.pubDate)
        item=item.to_dict()
        item['categorys']=item['category'].split(',')
        result.append(item)
    return result

def getArticle(articleId):
    article = Article.objects.filter(id=articleId)[0]
    return article

def getArticleNum():
    return Article.objects.count()
    
def getRecentArticles(num):
    recentArticles = getArticles(1, num)
    for article in recentArticles:
        article['url'] = "../article?articleid=%s" % article['id']
    return recentArticles


def getArticlesByCategory(page, num, articleCategory):
    items = Article.objects.order_by('-pubDate').filter(category=articleCategory)[(page - 1) * num: page * num]
    result = []
    for item in items:
        item=item.to_dict()
        result.append(item)
    return result

def getArticlesByTag(page, num, articleTag):
    items = Article.objects.order_by('-pubDate').filter(tag__contains=articleTag)[(page - 1) * num: page * num]
    result = []
    for item in items:
        item=item.to_dict()
        result.append(item)
    return result

def getArticleTag(tagName):
    if not ArticleTag.objects.filter(name=tagName):
        return None
    else:
        tag = ArticleTag.objects.filter(name=tagName)[0]
    return tag

def getArticleTags():
    return ArticleTag.objects.all()