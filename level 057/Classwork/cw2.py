def draw_stairs(n):
    new = ""
    for i in range(1, n+1):
        new += "I\n" + " " * i
    
    return new[:(-i - 1)]

print(draw_stairs(8))