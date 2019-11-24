from datetime import datetime
from dateutil import parser
from django.core.management import base
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
        for entry in feed.entries:
            self.get_or_create_item(instance, entry)

    def get_or_create_item(self, feed, entry):
        """Get or create Item."""
        guid = entry.get('id') or entry.get('link')
        try:
            # if Item already exists, do nothing.
            Item.objects.get(guid=guid)
        except Item.DoesNotExist:
            # retrieve publication date
            if entry.get('published') or entry.get('updated'):
                publication_date = parser.parse(
                    entry.get('published') or entry.get('updated'))
            else:
                publication_date = datetime.now()
            # create Item
            Item.objects.create(
                feed=feed,
                title=entry.title,
                description=entry.get('summary') or '',
                link=entry.link,
                guid=guid,
                publication_date=publication_date,
                retrieve_date=datetime.now())
