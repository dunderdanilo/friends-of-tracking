def transform_coordinates(x, y, direction='right', pitch_length=120, pitch_width=80):
    """
    Transforms from Statsbomb coordinates to the cartesian coordinates
    used by matplotlib.
    """
    if direction == 'right':
        return x, pitch_width - y

    if direction == 'left':
        return pitch_length - x, y

    raise ValueError(f'{direction} is not a valid direction.')
