from django.urls import path, include
from rest_framework import routers

from .views import CategoryListView


categories_urlpatterns = [
    path('', CategoryListView.as_view(), name='categories'),
]
