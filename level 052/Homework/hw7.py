# 7)დაწერეთ ფუნქცია index_of_max(lst), რომელიც აბრუნებს სიაში ყველაზე დიდი რიცხვის ინდექსს.

def index_of_max(lst):
    max = lst[0]
    for i in lst:
        if max < i:
            max = i
    
    return lst.index(max)

print(index_of_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))