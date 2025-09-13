def accum(st):
    New_string = ""
    for i in range(len(st)):
        if i == 0:
            New_string += st[i].upper()  
        else:
            New_string += "-" + st[i].upper() + st[i].lower() * i
    
    return New_string

print(accum("ZpglnRxqenU"))