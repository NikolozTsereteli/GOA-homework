# 3)დაწერეთ ფუნქცია double_numbers(lst), რომელიც აბრუნებს ახალ სიას, სადაც თითოეული ელემენტი ორმაგია.


def double_numbers(lst):
    New_list = []
    for i in lst:
        New_list.append(i * 2)
    
    return New_list

print(double_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))