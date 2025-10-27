# 6)დაწერეთ ფუნქცია multiples_of_five(lst), რომელიც აბრუნებს სიას, სადაც არის მხოლოდ ის რიცხვები, რომლებიც იყოფა 5–ზე და 3-ზე

def multiples_of_five(lst):
    New_list = []
    for i in lst:
        if i % 3 == 0 and i % 5 == 0:
            New_list.append(i)
    
    return New_list

print(multiples_of_five([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))