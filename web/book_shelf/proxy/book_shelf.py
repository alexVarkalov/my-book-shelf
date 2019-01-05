from django import forms

from django.contrib.admin import ModelAdmin

from book_shelf.models.book_shelf import BookShelf


class BookShelfProxy(BookShelf):
    class Meta:
        proxy = True
        verbose_name = 'Book Shelf'
        verbose_name_plural = 'Book Shelfs'


class BookShelfForm(forms.ModelForm):
    class Meta:
        model = BookShelfProxy
        exclude = []


class BookShelfAdmin(ModelAdmin):
    form = BookShelfForm

    fields = [
        'uuid',
        'created',
        'updated',
        'name',
        'books'
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
        'name'
    ]

    search_fields = (
        'name',
    )

    filter_horizontal = ('books',)