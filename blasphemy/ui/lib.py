import urwid


class Page:
    name = 'page'
    content = urwid.Text('page')

    width = ('relative', 80)
    align = 'center'
    height = ('relative', 80)
    valign = 'middle'

    def get_root_widget(self):
        return urwid.Padding(
            urwid.LineBox(
                urwid.Pile([
                    urwid.Text(('title', self.name), 'center'),
                    self.content
                ])
            ),
            width=self.width,
            align=self.align,
        )
