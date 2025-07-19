# Build a function that returns an array of integers from n to 1 where n>0.

# Example : n=5 --> [5,4,3,2,1]


def reverse_seq(n):
    New_list = []
    for i in range(n, 0, -1):
        New_list.append(i)
    
    return New_list

print(reverse_seq(5))