from datetime import datetime
from dateutil import parser
from django.core.management import base
from django.utils import timezone
import feedparser

from feed.models import Feed
from item.models import Item


class Command(base.BaseCommand):
    help = 'Retrieve feeds.'

    def handle(self, *args, **options):
        """Retrieve all Feeds."""
        for feed in Feed.objects.all():
            self.retrieve_feed(feed)
    
    def retrieve_feed(self, instance):
        """Retrieve and get or create Items."""
        feed = feedparser.parse(instance.feed)
        items = []
        for entry in feed.entries:
            guid = entry.get('id') or entry.get('link')
            try:
                # if Item already exists, do nothing.
                Item.objects.get(guid=guid)
            except Item.DoesNotExist:
                # retrieve publication date
                publication_date = parser.parse(
                    entry.get('published') or
                    entry.get('created') or
                    entry.get('updated'))
                # add Item to bulk create
                items.append(Item(
                    feed=instance,
                    title=entry.title,
                    description=entry.get('summary') or '',
                    link=entry.link,
                    guid=guid,
                    publication_date=publication_date,
                    retrieve_date=timezone.now()))
        # create Items
        Item.objects.bulk_create(items)
