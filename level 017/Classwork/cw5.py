# 5)შექმენით ფუნქცია რომელსაც გადაეცემა სია,თქვენი დავალებაა შეამოწმოთ თუ ამ სიის რომელიმე ელემენტის სიგრძე ნაკლებია 5 ზე ამოშალეთ ეს ელემენტები სიიდან და დააბრუნეთ ძველი სიასადაც აღარ გვექნება ამოშლილი სიტყვები რომელთა სიგრძეც ნაკლები იყო 5 ზე


def change_list(listt):
    New_list = []
    for i in listt:
        if len(i) >= 5:
            New_list.append(i)
    return New_list
    
print(change_list(["Presuppositions", "universals", "ethics", "time", "space", "past", "logic", "self"]))
