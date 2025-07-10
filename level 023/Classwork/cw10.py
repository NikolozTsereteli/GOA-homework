# 10)შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგებით სავსე სია,შენი დავალებაა გაიგო,თუ ეს სიტყვა არის capitalize მაგ შემთხვევაში დაამატა მსსგავსი სტრინგები სხვა სიაში,თუ სიტყვა არის upper დაამატე ეს სტრინგი სხვა ახალ სიაში,და თუ ეს სიტყვა არის lower მაშინ დაამატე ეს სიტყვები სხვა ახალ სიაში,შემდეგ სამივე სიაში მოცემული ელემენტები დააბრუნეთ ოღონდ სტრინგის სახით და თითოეული სტრინგი ერთმანეთსგან დაშორებული იიყოს $ ნიშნით


def create_new_lists(listt):
    New_list1 = []
    New_list2 = []
    New_list3 = []
    for char in listt:
        if char == char.capitalize():
            New_list1.append(char)
        elif char == char.upper():
            New_list2.append(char)
        elif char == char.lower():
            New_list3.append(char)

        capitalized_string = "$".join(New_list1)
        uppercase_string = "$".join(New_list2)
        lowercase_string = "$".join(New_list3)

    return capitalized_string, uppercase_string, lowercase_string
        
print(create_new_lists(["Cup", "Vase", "Bottle", "Fork", "spoon", "handkerchief", "plate", "TABLE", "CHAIRS"]))