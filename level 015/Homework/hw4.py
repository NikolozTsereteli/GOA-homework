# 4)შექმენი ფუნქცია რომელიც მომხმარებელს შემოატანინებს რიცხვს და სტრინგს,თქვენი დავლაებაა გამოიტანოთ მომხმარებლის შემოტანილი სტრინგიდან მომხმარებლის შემოტალინ რიცხვზე(ინდექსზე )მდგომი ასო


num = int(input("Enter a random number here: "))
text = input("Enter a random string here: ")
def character(num, text):
    print(text[num])

    return text, num

character(num, text)    


