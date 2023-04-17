class Workspace:
    def __init__(self):
        self.windows = []
    
    def add_window(self, win):
        self.windows.append(win)
    
    def remove_window(self, win):
        self.windows.remove(win)
    
    def get_windows(self):
        return self.windows
