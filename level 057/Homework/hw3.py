def nearest_sq(n):
    if n ** 0.5 == int(n ** 0.5):
        return n
    elif n - int(n ** 0.5) ** 2 > int(n ** 0.5 + 1) ** 2 - n:
        return int(n ** 0.5 + 1) ** 2
    else:
        return int(n ** 0.5) ** 2