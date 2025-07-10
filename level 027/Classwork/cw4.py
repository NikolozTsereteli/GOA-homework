# 4)შექმენით სია სადაც შეიყვანთ განსხვავებული მონაცემთთა ტიპის ელემენტებს,თქვენი დავალებაა ინტეჯერები ჩაამატო ერთ ახალ სიაშ და სტრინგები ჩაამატო სხვა ახალ სიაში


integer_list = []
string_list = []
listt = ["Nika", "Dato", 45, 67, 78, 56.67, 89.90, True, False, "Beqa"]
for char in listt:
    if type(char) == int:
        integer_list.append(char)
    elif type(char) == str:
        string_list.append(char)
print(integer_list, string_list)




