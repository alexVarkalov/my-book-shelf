from book_shelf.models.base import Base
from book_shelf.models.author import Author
from django.db import models

class Book(Base):
    title = models.CharField(
        max_length=255, 
        null=False,
    )
    author = models.ForeignKey(
        Author, 
        related_name='books', 
        on_delete=models.CASCADE,
    )
