# 3)შექმენით ფუნქცია რომელიც გაიგებს სიაში მყოფი ლუწი რიცხვების ჯამს


def sum(listt):
    sum = 0
    for i in listt:
        if i % 2 == 0:
            sum += i
    return sum

print(sum([1, 2, 3, 4, 5, 6]))