from django.shortcuts import render
from rest_framework import mixins, permissions, viewsets

from .models import Item
from .serializers import ItemSerializer


class ItemViewSet(
        mixins.ListModelMixin,
        mixins.UpdateModelMixin,
        viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
