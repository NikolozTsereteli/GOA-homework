# 2) შექმენით ფუნქცია რომელიც მომხმარებელის შემოატანილ რიცხვის ფაქტორიალს დააბრუნებს.


num = int(input("Enter your numbere here: "))
def factorial(num):
    Num = 1
    for i in range(1, num + 1):
        Num *= i
    return Num

print(factorial(num))

