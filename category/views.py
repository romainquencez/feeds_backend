from django.shortcuts import render
from rest_framework import generics, permissions

from .models import Category
from .serializers import CategorySerializer


class CategoryListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
