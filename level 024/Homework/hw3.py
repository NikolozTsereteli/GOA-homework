# 3)შექმენი ფუნქცია რომელსაც გადაეცემა სია,ამ სიაში უნდა გქონდეთ კიდევ სამი სია,და ამ სამ სიაში უნდა გქონდეთ სამ სამი ელემენტი,თქვენი დავალებაა მიწვდეთ ამ სიაში მყოფ სიას,შემდეგ ამ სიებში მყოფ ელმენტებს და შემდეგ ამ ელემენტებშ მყოფ ასოებს,შემდეგ ახალ სიაში დაამატე მხოლოდ ხმოვანი ასოები და დაასორტირე,დაალაგე ანბანის მიხედვით(არ არის სავალდებულო,შემდეგზე აგიხსნით მაგრამ ეცადეთ მოიძოთ,სორტირება)


def sort_lists(listt):
    New_list = []
    vowels = "aeiou"
    for list in listt:
        for words in list:
            for char in words:
                if char in vowels:
                    New_list.append(char)
                
    return sorted(New_list)

print(sort_lists([["nika", "luka", "nino"], ["ana", "dato", "gocha"], ["akaki", "levani", "ilia"]]))

