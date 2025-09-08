# 1)შექმენით ფუნქცია რომელიც გამოიტანს სიაში ლუწი რიცხვების ჯამს


def change(listt):
    sum = 0
    for i in listt:
        if i % 2 == 0:
            sum += i
    
    return sum



print(change([1, 2, 3, 4, 5, 6, 7]))