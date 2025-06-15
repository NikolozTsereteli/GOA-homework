# 3) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა მომხმარებელის შემოტანილი რიცხვი მნიშნველობად და გაარკვიეთ ამოდის თუ არა ფესვი არ მირცხვიდან.


num = int(input("Enter your number here: "))
sqrt = num ** 0.5
def square_root(num):
    if sqrt == int(sqrt):
        print(True)
    else:
        print(False)
    return sqrt

print(square_root(num))