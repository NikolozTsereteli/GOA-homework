# If you can't sleep, just count sheeps!!

# Task:
# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.


def count_sheep(n):
    counting_sheep = ""
    for i in range(1, n + 1):
        counting_sheep += str(i) + " sheep..."
    
    return counting_sheep

print(count_sheep(6))