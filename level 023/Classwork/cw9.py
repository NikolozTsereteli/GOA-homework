# 9)შექმენით ფუნქცია,რომელსაც გადაეცემა სტრინგებით სავსე სია,შენი დავალებაა შეამოწმო,თუ სტრინგი შეიცავს კენტი რაოდენობის ასობგერას,მაგ შემთხვევაში ჩაამატეთ ახალ სიაში,ხოლო თ შეიცავს ლუწი რაოდენობის ასობგერას შენი დავალებაა ესენიც ჩაამატო ახალ სიაშ ოღნდ მათ ასოები იყოს დიდი


def change_list(listt):
    New_list = []
    for char in listt:
        if len(char) % 2 != 0:
            New_list.append(char)
        else:
            New_list.append(char.upper())

    return New_list

print(change_list(["Nika", "GOA", "goa", "mshobeli", "cxovreba", "sikvdili", "wigni", "varjishi"]))