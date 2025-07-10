# 4)შექმენი ფუნქცია რომელსაც გადაეცემა სტრინგი,თქვენი დავალებაა ეს სტრინგი შემოატრიალოთ,შემდეგ კი ამ დააბრუნოთ შემოტრიალებული  სტრინგს რომ ქონდეს პირველი ასო 


def flip(stringg):
    New_string = stringg[::-1]
    print(New_string.capitalize())
    return New_string

(flip("python"))