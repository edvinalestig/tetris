# Define screen width and height
screen_width = 1920 / 1.2
screen_height = 1080 / 1.2

# Make an empty grid for the playing field
def empty_grid(cols, rows):
    ret = []

    # Append empty row
    for i in range(rows):
        ret.append([None] * cols)

    return ret

# Calculate a block size allowing the window to fit the screen
def grid_cell_width(cols, rows):
    return int(min(screen_width / cols, screen_height / rows))

def pos_is_on_grid(meta, x, y):
    if x < 0 or x > meta.cols - 1 or y > meta.rows - 1:
        return False
    return True
