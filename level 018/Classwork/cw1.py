# 1)შექმენი ფუნქცია რომელსაც გადაეცემა სხვადასხვა მონაცემეებით სავსე სია,თქვენი დავალებაა ახალ სიაში ჩააამატოთ მხოლოდ სტრინგ ტიპის მონაცემები


def all_types_list(listt):
    New_list = []
    for char in listt:
        if type(char) == str:
            New_list.append(char)
    
    return New_list

print(all_types_list(["Nika", 3, 4, 45, 56.67, "True", True]))