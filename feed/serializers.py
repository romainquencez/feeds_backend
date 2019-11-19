from rest_framework import serializers

from .models import Feed, Language


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ('id', 'title', 'icon')


class FeedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feed
        fields = ('id', 'title', 'website', 'language')
