# 8)შექმენი ფუნქცია სადაც მოათავსებთ სტრინგებს პატარა ასოებით,შენი დავალებაა ახალ სიაში დაამატო ეს სტრინგები მაგრამ ახალ სიაშ ჩაემატნონ დიდი ასოებით


def change_list(listt):
    New_list = []
    for char in listt:
        New_list.append(char.upper())
    
    return New_list

print(change_list(["nika", "saba", "akaki", "ilia", "sandro", "beqa"]))

