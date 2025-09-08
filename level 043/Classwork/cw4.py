def get_real_floor(n):
    if n <= 0:
        return n
    elif 13 >= n > 0:
        return n - 1
    else:
        return n - 2
    
print(get_real_floor(1))