import urwid

def callback():
    index = str(listBox.get_focus()[1])
    debug.set_text("Index of selected item: " + index)


debug = urwid.Text("Debug")

captions = "A B C D E F".split()
items = [urwid.Button(caption) for caption in captions]
walker = urwid.SimpleListWalker(items)
listBox = urwid.ListBox(walker)

urwid.connect_signal(walker, "modified", callback)

frame = urwid.Frame(body=listBox, header=debug)
urwid.MainLoop(frame).run()
