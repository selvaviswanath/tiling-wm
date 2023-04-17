from Xlib import X, Xutil


class Window:
    def __init__(self, display, win_id):
        self.display = display
        self.id = win_id
    
    def get_geometry(self):
        return self.id.get_geometry()
    
    def get_title(self):
        return self.id.get_wm_name()
    
    def move(self, x, y):
        self.id.configure(x=x, y=y)
    
    def resize(self, width, height):
        self.id.configure(width=width, height=height)
    
    def raise_window(self):
        self.id.configure(stack_mode=X.Above)
    
    def set_title(self, title):
        self.id.change_property(Xutil.Atom("_NET_WM_NAME"), Xutil.Atom("UTF8_STRING"), 8, title.encode('utf-8'))

    def interchange_left_right(self):
        left, _, right = self.get_neighbor_windows()
        if left:
            self.window.configure(
                x=left.get_geometry().x + left.get_geometry().width
            )
            left.window.configure(
                x=self.get_geometry().x + self.get_geometry().width
            )
        elif right:
            self.window.configure(
                x=right.get_geometry().x - self.get_geometry().width
            )
            right.window.configure(
                x=self.get_geometry().x - right.get_geometry().width
            )