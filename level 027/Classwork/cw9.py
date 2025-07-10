# 10)შექმენი ფუნქცია სადაც მოთავსებული გექნება სტრინგები,შენი დავალებაა რომ ეს სტრინგები გადაიყვანო ახალ სიაში მაგრამ მათ პირველი ასო იყოს დიდი ახალ სიაში


def change_list(listt):
    New_list = []
    for char in listt:
        New_list.append(char.capitalize())

    return New_list

print(change_list(["luka", "daviti", "goga", "kato", "ana"]))
