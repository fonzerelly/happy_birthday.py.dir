
def square (x):
    return x * x

def createCircle(position, radius):
    rSquared = square(radius)
    result = []
    for x in range (-radius, radius):
        for z in range(-radius, radius):
            if (square(x) + square(z) < rSquared):
                result.append((position.getX() + x, position.getY(), position.getZ() + z))

    return result

def createCandleLayer(position):
    return [
        (position.getX(), position.getY(), position.getZ() + 6),
        (position.getX() + 2, position.getY(), position.getZ() + 5),
        (position.getX() + 4, position.getY(), position.getZ() + 3),
        (position.getX() + 6, position.getY(), position.getZ()),
        (position.getX() + 5, position.getY(), position.getZ() - 2),
        (position.getX() + 3, position.getY(), position.getZ() - 4),
        (position.getX(), position.getY(), position.getZ() - 6),
        (position.getX() - 2, position.getY(), position.getZ() - 5),
        (position.getX() - 4, position.getY(), position.getZ() - 3),
        (position.getX() - 6, position.getY(), position.getZ()),
        (position.getX() - 5, position.getY(), position.getZ() + 2),
        (position.getX() - 3, position.getY(), position.getZ() + 4)

    ]

    