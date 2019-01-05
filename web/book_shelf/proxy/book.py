from django import forms

from django.contrib.admin import ModelAdmin

from book_shelf.models.book import Book


class BookProxy(Book):
    class Meta:
        proxy = True
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class BookForm(forms.ModelForm):
    class Meta:
        model = BookProxy
        exclude = []


class BookAdmin(ModelAdmin):
    form = BookForm

    fields = [
        'uuid',
        'created',
        'updated',
        'title',
        'author',
    ]

    readonly_fields = [
        'uuid',
        'created',
        'updated'
    ]

    list_display = [
        'uuid',
        'created',
        'updated',
        'title',
        'author',
    ]

    search_fields = (
        'firstname',
        'lastname',
    )
