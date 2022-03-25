import urwid


class App:
    palette = [
        ('footer', 'dark gray', 'black')
    ]

    pages = [
    ]

    page_widget = urwid.Filler(urwid.Divider(), 'top')

    def _get_menu(self):
        def button_handler(button, page):
            self.page_widget.original_widget = page.get_root_widget()

        button_widgets = []
        for page in self.pages:
            button = urwid.Button(page.name)
            urwid.connect_signal(button, 'click', button_handler, page)
            button_widgets.append(button)

        columns = urwid.Filler(
            urwid.GridFlow(button_widgets, 10, 2, 0, 'center'),
            'top'
        )
        return columns

    def _get_header(self):
        return urwid.Text('header', 'center')

    def _get_footer(self):
        return urwid.Text(('footer', 'footer'), 'center')

    def __init__(self):
        main_widget = urwid.Pile([
            self._get_menu(),
            ('weight', 80, self.page_widget),
        ])
        self.widget = urwid.Frame(
            main_widget,
            header=self._get_header(),
            footer=self._get_footer(),
        )

    def run(self):
        urwid.MainLoop(self.widget, self.palette).run()
