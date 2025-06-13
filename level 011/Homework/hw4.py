# 4) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვი შემდეგ კი მან უნდა დაგვიბრუნოს ეს რიცხვი დადებითია თუ უარყოფითი


def positive_or_negative(num):
    if num > 0:
        return str(num) + " is a positive number"
    elif num < 0:
        return str(num) + " is a negative number"
    else:
        return str(num) + " is neither positive nor negative"

result = positive_or_negative(0)
print(result)    
