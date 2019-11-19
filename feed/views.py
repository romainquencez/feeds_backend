from rest_framework import generics, mixins, permissions, viewsets

from .models import Feed, Language
from .serializers import FeedSerializer, LanguageSerializer


class LanguageListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


class FeedViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = FeedSerializer
    queryset = Feed.objects.all()
