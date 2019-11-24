from rest_framework import serializers

from item.serializers import ItemSerializer

from .models import Feed, Language


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ('id', 'title', 'icon')


class FeedSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, required=True)

    class Meta:
        model = Feed
        fields = ('id', 'title', 'website', 'language', 'items')
