def high_and_low(numbers):
    new_list = numbers.split()
    numbers2 = []
    for k in new_list:
        numbers2.append(int(k))
    
    max = numbers2[0]
    for i in numbers2:
        if i > max:
            max = i
            
    min = numbers2[0]
    for j in numbers2:
        if j < min:
            min = j
            
    return str(max) + " " + str(min)

print(high_and_low("1 2 3 4 5 6 7 8 9 10"))