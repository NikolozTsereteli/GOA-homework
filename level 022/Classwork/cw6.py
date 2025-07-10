# 6)შექმენით ფუნქცია რომესლსაც გადაეცემა რიცხვებით სავსე სია,თქვენი დავალებაა გაიგოთ ამ რიცხვების საშუალო არითმეყიკული,შემდეგ 0 დან ამ რიცხვამდე(საშუალო არითმეტიკული),იპოვეთ ყველა ლუწი რიცხვის ჯამი


def average_sum(listt):
    sum1 = 0
    amount = 0
    for i in listt:
        sum1 += 1
        amount += 1

    average = sum1 / amount

    sum2 = 0
    for j in range(0, int(average)):
        if j % 2 == 0:
            sum2 += i

    return sum2
            
print(average_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))