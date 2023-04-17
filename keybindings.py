from Xlib import X


def handle_key_press(display, event):
    keycode = event.detail
    if keycode == X.K_Left:
        # Handle left arrow key press
        pass
    elif keycode == X.K_Right:
        # Handle right arrow key press
        pass

    if event.state == Xlib.X.Mod4Mask:  # Windows key is pressed
        if event.keysym.lower() == "h":
            window = get_current_window()
            if window:
                window.move(-50, 0)
        elif event.keysym.lower() == "l":
            window = get_current_window()
            if window:
                window.move(50, 0)
        elif event.keysym.lower() == "j":
            window = get_current_window()
            if window:
                window.move(0, 50)
        elif event.keysym.lower() == "k":
            window = get_current_window()
            if window:
                window.move(0, -50)
    elif event.state == Xlib.X.ControlMask:
        if event.keysym.lower() == "q":
            sys.exit(0)


    if event.state == Xlib.X.Mod4Mask:  # Windows key is pressed
        if event.keysym.lower() == "h":
            if event.state & Xlib.X.ShiftMask:  # Shift key is pressed
                window = get_current_window()
                if window:
                    window.interchange_left_right()
            else:
                window = get_current_window()
                if window:
                    window.move(-50, 0)
        elif event.keysym.lower() == "l":
            if event.state & Xlib.X.ShiftMask:  # Shift key is pressed
                window = get_current_window()
                if window:
                    window.interchange_left_right()
            else:
                window = get_current_window()
                if window:
                    window.move(50, 0)
        elif event.keysym.lower() == "j":
            window = get_current_window()
            if window:
                window.move(0, 50)
        elif event.keysym.lower() == "k":
            window = get_current_window()
            if window:
                window.move(0, -50)
    elif event.state == Xlib.X.ControlMask:
        if event.keysym.lower() == "q":
            sys.exit(0)

            
def handle_key_release(display, event):
    pass


key_bindings = {
    X.KeyPress: handle_key_press,
    X.KeyRelease: handle_key_release,
}
