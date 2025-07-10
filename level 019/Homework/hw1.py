# 1) შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგად დიდი წინადადება. თქვენი მიზანია ეს წინადადება გახლიჩოთ და შეაერთოთ ისევ, ოღონდ ისე რომ თითოეული სიტყვის პირველი ასო იყოს დიდად


def change_string(stringg):
    words = stringg.split()
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    New_string = " ".join(words)

    return New_string

print(change_string("Epistemic justification is necessary for all set of beliefs and truth claims"))