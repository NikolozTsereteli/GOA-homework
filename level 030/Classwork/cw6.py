def square_sum(numbers):
    square_sum = 0
    for i in numbers:
        square_sum += i ** 2
    return square_sum

print(square_sum([1, 2, 2]))