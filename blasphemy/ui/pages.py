import urwid
from .lib import Page
from django.apps import registry


import os; os.unlink('/tmp/output.txt')
def debugger(message):
    with open('/tmp/output.txt', 'a') as outf:
        outf.write(message.rstrip() + '\n')


class FooPage(Page):
    name = 'Foo'

    def __init__(self):
        button = urwid.Button('test')

        def handler(button):
            raise urwid.ExitMainLoop()
        urwid.connect_signal(button, 'click', handler)

        self.content = urwid.Columns([
            urwid.Text('blah'),
            button,
            urwid.Text('blah'),
        ])


class BarPage(Page):
    name = 'Bar'
    content = urwid.Text('bar page', 'center')


class FilePage(Page):
    name = "File"

    def __init__(self):
        self.close_button = urwid.Button("quit")

        def close_handler(button):
            raise urwid.ExitMainLoop()

        urwid.connect_signal(self.close_button, 'click', close_handler)
        self.content = urwid.Columns([
            self.close_button,
            self.close_button
        ])


class DjangoAppsPage(Page):
    name = "Django apps"

    def __init__(self):
        app_names = registry.apps.get_app_configs().mapping.keys()

        def create_button(name, index):
            def handler(button):
                debugger(f'{button}: {index}')
            button = urwid.Button(name)
            urwid.connect_signal(button, 'click', handler)
            return button

        self.content = urwid.Pile([
            create_button(name, i)
            for i, name in enumerate(app_names)
        ])
