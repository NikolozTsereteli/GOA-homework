def twice_as_old(dad, son):
    age = 2 * son - dad
    if age >= 0:
        return age
    else:
        return -age

print(twice_as_old(48, 19))