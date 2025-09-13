def dont_give_me_five(start,end):
    length = 0
    for i in range(start, end + 1):
        if "5" not in str(i):
            length += 1
            
    return length

print(dont_give_me_five(1, 17))