def sum_digits(number):
    sum = 0
    for i in str(number):
        if i in "0123456789":
            sum += int(i)
        
    return sum

print(sum_digits(567))
        

