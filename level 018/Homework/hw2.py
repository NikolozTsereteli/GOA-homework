# 2)შექმენით ფუნქცია,რომელსაც გადაეცემა სტრინგებით სავსე სია,რომელი სტრინგის სიგრძეც მეტია 6 ზე დააბრუნეთ ეს სტრინგები ოღონდ შემოტრიალებული და პირველი ასო ქონდეთ დიდი(CAPITALIZE)


def flip_string(listt):
    for char in listt:
        if len(char) > 6:
            print(char[-1::-1].capitalize())
    
    return listt
            
(flip_string(["Nikoloz", "Nika", "Luka", "Lasha", "Metereveli", "Akaki", "Gabrieli"]))



