# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

# Return your answer as a number.


def sum_mix(arr):
    sum = 0
    for i in arr:
        if type(i) == int:
            sum += i
        else:
            sum += int(i)
    return sum

print(sum_mix([1, 2, 3, 4, 5, "6", "7", "8", "9", "10"]))

