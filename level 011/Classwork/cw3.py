# 3)შექმენით ფუნქცია რომელსაც არგუმენტად გადასცემთ სიას,თქვენი დავალებაა იპოვოთ ამ სიაში მყოფი რიცხვების ჯამი


def numbers(listt):
    sum = 0
    for i in listt:
        sum += i
    return sum    

print("Sum is", numbers([4, 57, 87, 35, 57, 788]))