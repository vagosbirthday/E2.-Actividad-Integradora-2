def closest_central(centrals, point):
    """
    Encuentra la central más cercana al punto dado.
    """
    min_distance = float('inf')
    closest = None

    for central in centrals:
        distance = ((central[0] - point[0]) ** 2 + (central[1] - point[1]) ** 2) ** 0.5
        if distance < min_distance:
            min_distance = distance
            closest = central

    return closest
