#9)შექმენი ფუნქცია რომელსაც გადაეცემა სია,თქვენი დავალებაა რომ ამ სიაში შეცვალოთ მესამე ინდექსზე მდგომი ელემენტი და ჩაანააცვლოთ "fortoxali" -ით


def change(listt):
    listt[3] = "fortoxali"
    return listt



print(change(["Vashli", "Kvaxi", "Banani", "Sazamtro", "Atami"]))
