from django.contrib import admin
from .proxy import (
    AuthorProxy, AuthorAdmin,
    BookProxy, BookAdmin,
    BookShelfProxy, BookShelfAdmin,
)
admin.site.register(AuthorProxy, AuthorAdmin)
admin.site.register(BookProxy, BookAdmin)
admin.site.register(BookShelfProxy, BookShelfAdmin)
