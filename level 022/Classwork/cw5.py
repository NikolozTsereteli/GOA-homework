# 5)შექმენით ფუნქცია რომელსაც გადაეცემა სია,ამ სიაში მოთავსებული იქნება როგორც სტრინგები ასევე ინტეჯერები,თქვენი დავალებაა გაიგოთ სოაში მყოფი სტრინგების რაოდენობა და ასევე უნდა გაიგოთ სიაში მყოფი ინტეჯერების ჯამი


def sum_amount(listt):
    amount = 0
    sum = 0
    for char in listt:
        if type(char) == str:
            amount += 1
        else:
            sum += char

    return amount, sum

print(sum_amount([19, "Nika", 16, "Maia", 87, "Meri", 369, "???"]))
