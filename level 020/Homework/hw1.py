# 1)შექმენით ფუნქცია რომელსაც გადაეცემა სახელებით სავსე სია,თქვენი დავალებაა გამოიტანოთ ამ სიაში მყოფი სახელების თითოეული ასო


def all_characters(listt):
    for char in listt:
        for i in char:
            print(i)
            
    return listt

(all_characters(["Nika", "Luka", "Gabrieli", "Mate", "Ioane", "Akaki"]))