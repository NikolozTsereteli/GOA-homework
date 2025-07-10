# 15)შექმენი ფუნქცია რომელსაც გადაეცემა სია,შენი დავალებაა ეს სია აქციო სტრინგად დად თითოეული ელემენტი დაშორებული იყოს # ამ ნიშნით,შემდეგ გადაუარეთ ამ სტრინგს და დაითვალეთ თუ რამდენჯერ გვხვდება # ეს ნიშანი შენს სტრინგში


def change_list(listt):
    New_string = "#".join(listt)
    count = 0
    for char in New_string:
        if char == "#":
            count += 1

    return count

print(change_list(["I", "am", "19", "years", "old"]))


