import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from window import Window
from workspace import Workspace

class TilingWindowManager:
    def __init__(self):
        self.workspaces = [Workspace()]

    def add_workspace(self):
        self.workspaces.append(Workspace())

    def remove_workspace(self, workspace):
        self.workspaces.remove(workspace)

    def move_window_to_workspace(self, window, workspace_index):
        self.workspaces[workspace_index].add_window(window)

    def move_window_left(self, window):
        pass

    def move_window_right(self, window):
        pass

    def resize_window_left(self, window):
        pass

    def resize_window_right(self, window):
        pass

if __name__ == "__main__":
    twm = TilingWindowManager()
    Gtk.init()
    win = Gtk.Window()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
