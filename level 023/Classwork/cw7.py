# 7)შექმენით ფუნქცია რომელიც ამოშლის სიიდან ლუწ ინდექსზე მდგომ ელემენტებს , და კენტ ინდექსზე მდგომ ელემენტებს ჩაამატებს ახალ სიაში


def remove_even(listt):
    New_list = []
    for i in range(len(listt)):
        if i % 2 != 0:
            New_list.append(listt[i])
    
    return New_list

print(remove_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))