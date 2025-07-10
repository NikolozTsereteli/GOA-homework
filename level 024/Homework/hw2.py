# 2)შექმენი ფუნქცია რომელსაც გადაეცემა სია,ამ სიაში უნდა იყოს მოთავსებული სახელები,თქვენი დავალებაა მიწვდეთ ამ სახელებს და შემდეგ ამ სახელებში მყოფ ასოებს,თქვენი დავალებაა ახალ სიაში ჩაამატოთ მხოლოდ თანხმოვანია ასოები,შემდეგ ამ სიაში მყოფი ასოები დაალაგეთ ანბანის მიხედვით(დაასორტირეთ)მოიძეთ ინფორმაცია თუ როგორ ხდება სორტირება და რომელი ფუნქცია გამოიყენება ამისათვის


def change_list(listt):
    New_list = []
    consonants = "bcdfghjklmnpqrstvwxyz"
    for word in listt:
        for char in word:
            if char.lower() in consonants:
                New_list.append(char)
    sorted_list = sorted(New_list)

    return sorted_list

print(change_list(["nika", "maia", "marina", "zura", "gela", "savle", "buxa", "aleko"]))