# 2) შექმენით ფუნქცია რომელსაც გადაეცემა სხვადასხვა მონაცემთა ტიპით სავსე სია, თქვენი მიზანია ამ სიიდან მარტო სტრინგ ტიპის მონაცემები დააბრუნოთ ახალ სიაში


def change_list(listt):
    New_list = []
    for char in listt:
        if type(char) == str:
            New_list.append(char)

    return New_list

print(change_list([1, 2, 3, 45.67866564, 0, "Me", "Science", True and False, "False", "Epistemic justification", "Logical Fallacy"]))