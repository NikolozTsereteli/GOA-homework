# 8)დაწერეთ ფუნქცია total_length(words), რომელიც აბრუნებს სიაში არსებული ყველა სტრინგის სიგრძეების ჯამს.

def total_length(words):
    total = 0
    for i in words:
        if type(i) == str:
            total += len(i)
    
    return total

print(total_length(["Nice", "WoW", 567, True, False, "Aristotle", "Kant"]))