# 5)შექმენი ფუნქცია რომელსაც გადასცემ სიას,თქვენი დავალებაა ახალ სიაში დაამატოთ ეს სახელები ოღონდ ყველა ასო იყოს დიდი ამ სტრინგებში


def change_list(listt):
    New_list = []
    for char in listt:
        New_list.append(char.upper())
        
    return New_list

print(change_list(["Nika", "Goga", "Dato", "akaki", "lasha", "beqa", "marina"]))