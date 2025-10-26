def pythagorean_triple(i):
    new = sorted(i)
    if new[0] ** 2 + new[1] ** 2 == new[2] ** 2:
        return True
    else:
        return False