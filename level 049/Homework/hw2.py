def factorial(n):
    factorial = 1
    if n < 0 or n > 12:
        raise ValueError("n must be between 0 and 12!")
    elif n == 0:
        return 1
    else:
        for i in range(n):
            factorial *= i + 1
    return factorial

print(factorial(30))
        

