# 3)შექმენი ფუნქცია,რომელსაც გადაეცემა სია ამ სიაში იქნება მოთავსებული პატარა ასოებით დაწერილი სახელები,თქვენი დავალებაა ახალ სიაში დაამატოთ ყველა ელემენტი ოღონდ ისინი უნდა იყოს დიდი ასოებით დაწერილი


def uppercase(listt):
    New_list = []
    for char in listt:
        New_list.append(char.upper())

    return New_list

print(uppercase(["nika", "maia", "medea", "marina", "zura", "meri"]))