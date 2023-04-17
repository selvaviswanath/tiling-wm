def tile_horizontally(windows, x, y, width, height):
    # Calculate the width of each window
    window_width = width // len(windows)
    for i, win in enumerate(windows):
        # Calculate the x position of the window
        win_x = x + i * window_width
        # Move and resize the window
        win.move(win_x, y)
        win.resize(window_width, height)
