# In this kata, your job is to return the two distinct highest values in a list. If there're less than 2 unique values, return as many of them, as possible.

# The result should also be ordered from highest to lowest.

# Examples:

# [4, 10, 10, 9]  =>  [10, 9]
# [1, 1, 1]  =>  [1]
# []  =>  []


def two_highest(arg1):
    if arg1 == []:
        return []
    
    unique = []
    for num in arg1:
        if num not in unique:
            unique.append(num)
    
    if len(unique) == 1:
        return [unique[0]]
    
    max1 = unique[0]
    for num in unique:
            if num > max1:
                max1 = num
    unique.remove(max1)
    
    max2 = unique[0]
    for num in unique:
        if num > max2:
            max2 = num
    
    return [max1, max2]

print(two_highest([1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8, 8, 9, 9]))