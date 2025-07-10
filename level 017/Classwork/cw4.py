# 4)შექმენით ფუნქცია რომესლაც გადაეცემათ სტრინგი,თქვენი დავალებაა შეამოწმოთ თუ ამ სტრინგის პირველი ასო იქნება uppercase ანუ დიდი მაგ შემთხვევაში დააბრუნეთ True სხვა შემთხვევეაში დააბრუნეთ False


def true_or_false(stringg):
    if stringg == stringg.capitalize():
        print(True)
    else:
        print(False)

    return stringg

(true_or_false("Nikolozi"))