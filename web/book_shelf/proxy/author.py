from django import forms

from django.contrib.admin import ModelAdmin

from book_shelf.models.author import Author


class AuthorProxy(Author):
    class Meta:
        proxy = True
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class AuthorForm(forms.ModelForm):
    class Meta:
        model = AuthorProxy
        exclude = []


class AuthorAdmin(ModelAdmin):
    form = AuthorForm

    fields = [
        'uuid',
        'created',
        'updated',
        'firstname',
        'lastname',
    ]

    readonly_fields = [
        'uuid',
        'created',
        'updated',
    ]

    list_display = [
        'uuid',
        'created',
        'updated',
        'firstname',
        'lastname',
    ]

    search_fields = (
        'firstname',
        'lastname',
    )
