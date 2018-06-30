from website.models import Article
from website.models import Book

def getArticles(page, num):
    items = Article.objects.order_by('-pubDate').all()[(page - 1) * num: page * num]
    result = []
    for item in items:
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

def getArticleCategories():
    result = {}
    for item in Article.objects.all():
        try:
            keys = item.category.split(',')
        except:
            continue
        for key in keys:
            try:
                result[key] += 2
            except:
                result[key] = 10
    return result

def getArticlesByCategory(category):
    articles = Article.objects.order_by('-pubDate').all()
    result = []
    for item in articles:
        if category in item.category:
            item = item.to_dict()
            item['categorys'] = item['category'].split(',')
            result.append(item)
    return result