# 5)შექმენი ფუნქცია რომელსაც გადაეცემა სია,თქვენი დავალებაა სიიდან ამოშალოთ მხოლოდ ის სიტყვები რომლის სიგრძეც ნაკლებია 5 ზე


def remove(listt):
    for char in listt:
        if len(char) < 5:
            listt.remove(char)
    return listt

print(remove(["Nika", "Kompiuteri", "GOA", "Sporti", "Boxi", "Ping Pongi"]))