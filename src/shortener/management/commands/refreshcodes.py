from django.core.management.base import BaseCommand, CommandError

from shortener.models import shortenURL

class Command(BaseCommand):
    help = 'Refreshes all shortCodes'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        return shortenURL.objects.refresh_shortcodes(items=options['items'])