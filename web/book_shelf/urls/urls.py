from django.conf.urls import url, include

from book_shelf.urls.author import urlpatterns as author_urls


urlpatterns = [
    url(r'book_shelf/',
        include(
            author_urls,
        ),
        name='book_shelf')
]
