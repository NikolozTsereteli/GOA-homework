# 17)შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგებით სავსე სია,შენი დავალებაა შეამოწმო თუ რამდენი ცალი დიდი ასო ურევია ყველა სტრინგში მთლიანად


def count_list(listt):
    count = 0
    for name in listt:
        for char in name:
            if char == char.upper():
                count += 1
    
    return count

print(count_list(["me", "Shen", "Is", "Chven", "Isini"]))

