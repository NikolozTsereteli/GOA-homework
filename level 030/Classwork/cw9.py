def move_zeros(lst):
    for i in lst:
        if i == 0:
            lst.remove(0)
            lst.append(0)
            
    return lst

print(move_zeros([1, 2, 0, 4, 5, 0, 6, 7, 0]))