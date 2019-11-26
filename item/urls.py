from django.urls import path, include
from rest_framework import routers

from .views import ItemViewSet, LastestItemsListView


router = routers.DefaultRouter()

router.register('', ItemViewSet, base_name='items')

items_urlpatterns = [
    path('latest/', LastestItemsListView.as_view(), name='latest_items'),
    path('', include(router.urls)),
]
