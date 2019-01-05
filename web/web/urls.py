import coreapi
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view

from book_shelf.urls.urls import urlpatterns as book_shelf_urls


from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='SWAGGER API')
rest_schema_view = get_schema_view(title='API', )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include(book_shelf_urls)),
    url(r'^api/', rest_schema_view),
    url(r'^swagger/$', schema_view),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
