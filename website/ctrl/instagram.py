from website.models import MediaInstagram

def getPhotos():
    items = MediaInstagram.objects.order_by('-uploadDate').all()
    result = []
    for item in items:
        item=item.to_dict()
        result.append(item)
    return result