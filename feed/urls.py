from django.urls import path, include
from rest_framework import routers

from .views import FeedViewSet, LanguageListView

router = routers.DefaultRouter()

router.register('', FeedViewSet, base_name='feeds')

feeds_urlpatterns = [
    path('languages/', LanguageListView.as_view(), name='languages'),
    path('', include(router.urls)),
]
