# 2)დაწერეთ ფუნქცია categorize_numbers(lst), რომელიც იღებს რიცხვების სიას და ამოწმებს თუ რიცხვი:

# "positive" – დადებითი რიცხვები

# "negative" – უარყოფითი რიცხვები

# "zero" – ნულების რაოდენობა


def categorize_numbers(lst):
    New_list = []
    for i in lst:
        if i > 0:
            New_list.append("positive")
        elif i < 0:
            New_list.append("negative")
        else:
            New_list.append("zero")
    
    return New_list

print(categorize_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 0]))