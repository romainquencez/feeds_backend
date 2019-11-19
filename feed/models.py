from django.db import models


class Language(models.Model):
    title = models.CharField(max_length=150, blank=True)
    icon = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title


class Feed(models.Model):
    title = models.CharField(max_length=150, blank=True)
    feed = models.URLField()
    website = models.URLField(null=True)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
