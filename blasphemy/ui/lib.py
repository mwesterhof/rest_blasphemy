import urwid


class Page:
    name = 'page'
    content = urwid.Filler(urwid.Text('page'))
    width = ('relative', 80)
    align = 'center'
    height = ('relative', 80)
    valign = 'middle'

    def get_root_widget(self):
        return urwid.Padding(
            urwid.LineBox(
                self.content
            ),
            width=self.width,
            align=self.align,
        )
