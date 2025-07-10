# 8)შექმენი ფუნქცია რომელსაც გადაეცემა სია,შენი დავალებაა იპოვო ამ სიიდან ლუწი რიცხვები და ჩაამატო ახალ სიაში,შემდეგ ამ სიიდან უნდა გაიგოთ კენტ ინდექსზე მდგომი რიცხვების კვადრატების ჯამი


def sum_of_squares(listt):
    New_list = []
    for i in listt:
        if i % 2 == 0:
            New_list.append(i)

    sum = 0
    for j in range(len(New_list)):
        if i % 2 != 0:
            sum += j * j
    
    return sum

print(sum_of_squares([13, 23, 34, 45, 56, 65, 76, 87, 89, 68, 57, 37, 35, 34, 53]))