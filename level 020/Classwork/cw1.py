# 1)შექმენით ფუნქცია რომელსაც გადაეცემა სახელები,თქვენი დავალებაა ტერმინალში გამოიტანოთ კენტ ინდექსზე მდგომი სახელები და შეინახოთ ახალ სიაში


def change_list(listt):
    New_list = []
    for i in range(len(listt)):
        if i % 2 != 0:
            New_list.append(listt[i])

    return New_list
        
print(change_list(["Nika", "Goga", "Gabrieli", "Ana", "Elene"]))