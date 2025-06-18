# 1)შექმენი ფუნქცია რომელსაც გადაეცემა სტრინგი,შენი დავალებაა ამ სტრინგიდან ამოშალო კენტ იდექსზე მდგომი ასოები და დააბრუნო სტრინგი მათ გარეშე


def even_string(text):
    New_string = ""
    for i in range(len(text)):
        if i % 2 == 0:
            New_string += text[i]
    return New_string



print(even_string("Nikolozi"))