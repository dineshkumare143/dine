def pow(x, y):

    power = x

    if y == 0:
        return 1

    while y > 1:
        power *= x

        y -= 1

    return power
