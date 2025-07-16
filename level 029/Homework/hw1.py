# Task: You get an array of numbers, return the sum of all of the positives ones. 
# Example: [1, -4, 7, 12] => 1 + 7 + 12 = 20  Note: If there is nothing to sum, sum is default to 0. 


def positive_sum(arr):
    if arr == []:
        return 0
    
    sum = 0
    for i in arr:
        if i > 0:
            sum += i
            
    return sum

print(positive_sum([1, 2, 3, -6, -7, 0]))

