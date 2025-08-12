# 1)შექემენით ფუნქცია რომელსაც გადაეცემა რიცხვებიტ სავსე სია,თქვენი დავალებაა ამ სიიდან ამოშალოთ ლუწი რიცხვები

def change_list(listt):
    New_list = []
    for i in (listt):
        if i % 2 != 0:
            New_list.append(i)
    
    return New_list


print(change_list([1, 2, 3, 4, 5, 6, 7, 8]))