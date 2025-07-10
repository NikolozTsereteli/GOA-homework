# 4)შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგი,თქვენი დავალებაა რომ ამ სტრინგიდან ამოიღოთ მხოლოდ ხმოვანი ასოები და შეინახოთ ერთად ცვლადში,შემდეგ კი ეს ამოღებული ასოები გადააქციეთ დიდ ასოებათ და ისე დააბრუნეთ


def vowel_string(stringg):
    New_string = ""
    vowels = "aeiou"
    for char in stringg:
        if char in vowels:
            New_string += char.upper()

    return New_string
    
print(vowel_string("Nikolozi"))