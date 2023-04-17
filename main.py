from Xlib import display, X
from window import Window
from workspace import Workspace
from keybindings import key_bindings
from layout import tile_horizontally


def main():
    # Open a connection to the X server
    d = display.Display()

    # Create a window
    win = d.create_resource_object('window', d.create_window(
        d.screen().root,   # Parent window
        0, 0,               # X, Y position
        640, 480,           # Width, height
        0,                  # Border width
        d.screen().root_depth,  # Color depth
        X.InputOutput       # Window class
    ))

    # Map the window to the screen
    win.map()

    # Create a workspace for the window
    workspace = Workspace()
    workspace.add_window(Window(d, win))

    # Grab the keyboard to listen for key events
    win.grab_keyboard(True, X.GrabModeAsync, X.GrabModeAsync, X.CurrentTime)

    # Run the event loop
    while True:
        event = d.next_event()
        if event.type in key_bindings:
            key_bindings[event.type](d, event)
        elif event.type == X.ConfigureNotify:
            # Update the layout when the window is resized
            geometry = win.get_geometry()
            tile_horizontally(workspace.get_windows(), geometry.x, geometry.y, geometry.width, geometry.height)
