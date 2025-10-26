def how_much_water(water, load, clothes):
    if clothes > load * 2:
        return "Too much clothes"
    elif clothes < load:
        return "Not enough clothes"
    return round(water * 1.1 ** (clothes - load), 2)

print(how_much_water(5, 7, 8))