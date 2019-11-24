from django.db import models

from feed.models import Feed

class Item(models.Model):
    feed = models.ForeignKey(
        Feed, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    link = models.URLField(max_length=500)
    guid = models.CharField(max_length=500, unique=True)
    publication_date = models.DateTimeField()
    retrieve_date = models.DateTimeField(null=True)
    read = models.BooleanField(default=False)
