# 7)შექმენი ფუნქცია რომელსაც გადაეცემა სტრინგი --> giorgi nozadze,თქვენი დავალებაა რომ დააბრუნოთ ამ სახელი გვარის ინიციალები ოღონდ დიდი ასოებით ასეთი ფორმატით G.N


def innitials(stringg):
    New_list = stringg.split(" ")
    New_list2 = []
    for name in New_list:
        New_list2.append(name[0].upper())

    New_string = ".".join(New_list2)
    return New_string


print(innitials("giorgi nozadze"))