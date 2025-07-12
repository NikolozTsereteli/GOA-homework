# Write a function which calculates the average of the numbers in a given array.

# Note: Empty arrays should return 0.


def find_average(numbers):
    if numbers == []:
        return 0
    
    sum = 0
    amount = 0
    for i in numbers:
        sum += i
        amount += 1
    return sum/amount

print(find_average([1, 2, 3, 4, 5]))