# 6)შექმენი ფუნქცია რომელსაც გადაეცემა სია,ამ სიაში მოთავსებული უნდა იყოს როგორც სტრინგები ასევე ინტეჯერები,შენი დავალებაა სიიდან ამოშალო მხოლოდ სტრინგის ტიპის ელემენტები,რაც შეეხება ინტეჯერებს ჩაამატეთ ახალ სიაში


def change_list(listt):
    New_list = []
    for char in listt:
        if type(char) == int:
            New_list.append(char)

    return New_list

print(change_list([23, 34, 45, 56, "Greg", "John", "Bob", "Josh"]))