def filter_list(l):
    New_list = []
    for i in l:
        if type(i) == int:
            New_list.append(i)
            
    return New_list

print(filter_list([1, 2, 'aasf', '1', '123', 123]))

