import uuid
from django.db import models


class Base(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True,
    )

    created = models.DateTimeField(
        verbose_name='Date',
        auto_now_add=True,
        null=True,
        blank=True,
    )

    updated = models.DateTimeField(
        verbose_name='Update',
        auto_now=True,
    )

    class Meta:
        abstract = True
