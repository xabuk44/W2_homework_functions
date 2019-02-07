
def roll_quantity (wall_length, wall_width, wall_height, wallpaper_length, wallpaper_width):
    """
    >>> roll_quantity(5, 6, 2.75, 10, 1.06) #doctest:+ELLIPSIS
    8...
    """
    wall_height += 0.1
    room_perimetr = (wall_length + wall_width) * 2
    cloth_quantity = int(round(room_perimetr / wallpaper_width))
    cloth_in_one_roll = int(wallpaper_length / wall_height)
    roll_quantity = int(cloth_quantity / cloth_in_one_roll) + 1
    return roll_quantity

if __name__ == "__main__":
    import doctest
    doctest.testmod()

