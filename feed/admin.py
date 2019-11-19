from django.contrib import admin

from .models import Feed, Language


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('icon', 'title')
    list_per_page = 20


@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ('title', 'website', 'language')
    list_per_page = 20
