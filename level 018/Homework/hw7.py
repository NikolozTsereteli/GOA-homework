# 7)შექმენით ფუნქცია რომელსაც გადაეცემა სია,თქვენი დავალებაა იპოვოთ ამ სიაში მხოლოდ ლუწ ინდექსზე მდგომი ელემენტების საშუალო არითმეტიკული


def average(listt):
    sum = 0
    amount = 0
    for i in range(len(listt)):
        if i % 2 == 0:
            sum += listt[i]
            amount += 1
    
    return sum / amount

print(average([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))