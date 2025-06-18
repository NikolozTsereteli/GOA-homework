# 3)შექმენი ფუნქცია როომელსაც გადაეცემა სტრინგი --> fortoxali,თქვენი დავალებაა დააბრუნოთ თითოეული ასოს ინდექსი სიის სახით (არ გამოიყენოთ len ფუნქცია)


def index(stringg):
    New_list = []
    i = 0
    for char in stringg:
        New_list.append(i)
        i += 1

    return New_list

print(index("fortoxali"))