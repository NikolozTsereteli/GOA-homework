def kata_13_december(lst):
    lst2 = []
    for i in lst:
        if i % 2 != 0:
            lst2.append(i)
    
    return lst2

print(kata_13_december([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
