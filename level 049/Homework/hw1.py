def small_enough(array, limit):
    for i in array:
        if i > limit:
            return False
    return True

print(small_enough([78, 117, 110, 99, 104, 117, 107, 115], 100))

