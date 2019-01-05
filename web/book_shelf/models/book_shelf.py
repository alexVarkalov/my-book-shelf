from book_shelf.models.base import Base
from book_shelf.models.book import Book
from django.db import models


class BookShelf(Base):
    name = models.CharField(
        max_length=255,
    )
    books = models.ManyToManyField(
        Book,
        related_name='shelfs',
    )
