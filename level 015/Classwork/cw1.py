# 1)შექმენი ფუნქცია,რომელსაც გადაეცემა სტრინგი --> aleqsandre , თქვენი დავალებაა დააბრუნოთ კენტ ინდექსზე მდგომი ასოები


def odd_string(text):
    New_text = ""
    for i in range(len(text)):
        if i % 2 == 1:
            New_text += text[i]
    return New_text

print(odd_string("aleqsandre"))
