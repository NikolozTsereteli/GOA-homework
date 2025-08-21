def find_short(s):
    new_list = s.split(" ")
    min = len(new_list[0])
    for char in new_list:
        if len(char) < min:
            min = len(char)
    
    return min

print(find_short("I have many great friends."))