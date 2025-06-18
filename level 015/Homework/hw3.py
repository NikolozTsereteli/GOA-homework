# 3)შექმენი ფუნქცია რომელსაც გადაეცემა სტრინგი --> "hidroeleqtrosadguri" ,თქვენი დავალებაა ამოშალოთ ამ სტრინგიდან მხოლოდ ხმოვნები და დააბრუნოთ ეს სტრინგი ხმოვნების 


def text(stringg):
    xmovnebi = "aeiou"
    New_string = ""
    for char in stringg:
        if char not in xmovnebi:
            New_string += char
            

    return New_string

print(text("hidroeleqtrosadguri"))


