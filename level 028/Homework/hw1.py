# Complete the square sum function so that it squares each number passed into it and then sums the results together.

# For example, for [1, 2, 2] it should return 9


def square_sum(numbers):
    square_sum = 0
    for i in numbers:
        square_sum += i * i

    return square_sum

print(square_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))