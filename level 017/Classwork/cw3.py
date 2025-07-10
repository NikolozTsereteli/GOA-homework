# 3)შექმენით ფუნქცია რომელსაც გადაეცემა სია,თქვენი დავალებაა გადაააქციოთ ეს სიაერთ დიდ სტრინგად და ეს სიტყვები ერთმანეთსგან გამოყავით სფეისებით,გამოიყენე შესაბამის ფუნქცია გაიხსენეთ


def list_to_string(listt):
    words = ""
    words = " ".join(listt)
    return words

print(list_to_string(["Love", "Justice", "Ethics", "Morality", "Truth", "Value"]))

