# Create a function with two arguments that will return an array of the first n multiples of x.

# Assume both the given number and the number of times to count will be positive numbers greater than 0.

# Return the results as an array or list ( depending on language ).

# Examples
# x = 1, n = 10 --> [1,2,3,4,5,6,7,8,9,10]
# x = 2, n = 5  --> [2,4,6,8,10]


def count_by(x, n):
    New_list = []
    for i in range(x, x * n + 1, x):
        New_list.append(i)
        
    return New_list

print(count_by(5, 6))