# 16)შექმენი ფუნქცია რომელსაც გადაეცემა რიცხვებით სავსე სია,შენი დავალებაა ახალ სიაში ჩაამატო კენტი რიცხვები,შემდეგ ამ ახალ სიაში მყოფი რიცხვების საშუალო არითმეტიკული გიაგეთ


def change_list(listt):
    New_list = []
    for i in listt:
        if i % 2 != 0:
            New_list.append(i)
    
    sum = 0
    amount = 0
    for i in New_list:
        sum += i
        amount += 1

    return sum / amount

print(change_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))