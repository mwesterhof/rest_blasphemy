from .pages import FilePage, FooPage, BarPage, DjangoAppsPage
from .app import App


class MyApp(App):
    pages = [
        FilePage(),
        DjangoAppsPage(),
    ]
