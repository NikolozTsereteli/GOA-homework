def unique_sum(lst):
    sum = 0
    
    if lst == []:
        return None
    
    else:
        for i in set(lst):
            sum += i
            
    return sum

print(unique_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
            
            
            

