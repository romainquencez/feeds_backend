from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from feed.urls import feeds_urlpatterns
from item.urls import items_urlpatterns
from category.urls import categories_urlpatterns

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="Documentation",
        terms_of_service=""
    ),
    public=True,
    permission_classes=(permissions.IsAdminUser, )
)

api_urlspatterns = [
    path('feeds/', include(feeds_urlpatterns)),
    path('items/', include(items_urlpatterns)),
    path('categories/', include(categories_urlpatterns)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlspatterns), name='api'),
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(
        r'^docs/$',
        schema_view.with_ui('swagger', cache_timeout=0), name='docs')
]
