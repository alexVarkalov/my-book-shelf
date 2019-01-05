from book_shelf.models.base import Base
from django.db import models

class Author(Base):
    firstname = models.CharField(
        max_length=255,
        null=False,
    )
    lastname = models.CharField(
        max_length=255,
        null=False,
    )

    def __str__(self):
        return '{} {}'.format(self.firstname, self.lastname)
