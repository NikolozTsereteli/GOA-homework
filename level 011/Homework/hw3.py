# 3) შექმენით ფუნქცია რომელსაც გადაეცემა არგუმენტად რიცხვი შემდეგ კი მან უნდა დაგვიბრუნოს ლუწია ეს რიცხვი თუ კენტი


def odd_or_even(num):
    if num % 2 == 0:
        return str(num) + " is even"
    else:
        return str(num) + " is odd"

result = odd_or_even(3)
print(result)    

