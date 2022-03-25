from . import pages as page_classes
from .app import App


class MyApp(App):
    pages = [
        page_classes.FilePage(),
        page_classes.ProjectPage(),
        page_classes.DjangoAppsPage(),
        page_classes.DjangoSettingsPage(),
    ]
