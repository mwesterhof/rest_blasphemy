from django.core.management.base import BaseCommand

from blasphemy.ui.fancy import MyApp


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        MyApp().run()
