from django.shortcuts import render
from rest_framework import generics, mixins, permissions, viewsets

from .models import Item
from .serializers import ItemSerializer


class ItemViewSet(
        mixins.ListModelMixin,
        mixins.UpdateModelMixin,
        viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class LastestItemsListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ItemSerializer
    queryset = Item.objects.order_by('-publication_date')[:100]
