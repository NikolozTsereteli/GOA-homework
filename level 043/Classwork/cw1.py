def sum_mul(n, m):
    total = 0
    if m <= 0 or n <= 0:
        return "INVALID"
    
    for i in range(m):
        if i % n == 0:
            total += i
    
    return total

print(sum_mul(1, 5634))