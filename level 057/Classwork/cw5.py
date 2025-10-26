def powers_of_two(n):
    new_list = []
    for i in range(n+1):
        new_list.append(2**i)
    
    return new_list

print(powers_of_two(100))

