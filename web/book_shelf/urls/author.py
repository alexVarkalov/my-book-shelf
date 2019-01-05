from django.conf.urls import url

from book_shelf.views.author import AuthorViewSet

urlpatterns = [
    url(r'^author/$', AuthorViewSet.as_view({'get': 'list', 'post': 'create'}), name='author-list'),
    url(r'^author/(?P<uuid>[0-9a-f-]+)$', AuthorViewSet.as_view({'get': 'retrieve'}), name='author-detail'),
]
