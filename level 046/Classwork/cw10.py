def number(lines):
    New_list = []
    i = 1
    for char in lines:
        New_list.append(str(i) + ": " + char) 
        i += 1
    
    return New_list

print(number(["a", "b", "c"]))