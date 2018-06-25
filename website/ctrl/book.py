from website.models import Book


def getBooks(page, num):
    items = Book.objects.order_by('-uploadDate').all()[(page - 1) * num:page * num]
    result = []
    for item in items:
        item = item.to_dict()
        item['categorys'] = item['category'].split(',')
        result.append(item)
    return result


def getBook(book_id):
    book = Book.objects.filter(id=book_id)[0]
    return book


def getRecentBooks(num):
    recentBooks = getBooks(1, num)
    for book in recentBooks:
        book['url'] = "../book?bookid=%s" % book['id']
    return recentBooks

def getBooksByCategory(category):
    books = Book.objects.order_by('-uploadDate').all()
    result = []
    for book in books:
        if category in book.category:
            item = book.to_dict()
            item['categorys'] = item['category'].split(',')
            result.append(item)
    return result