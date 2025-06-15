# 3) შექმენით ფუნქცია რომელსაც არგუმენტად სია, ამ სიაში უნდა იყოს სხვადასხვა ტიპის მონაცემები და დაითვალოს რამდენი სტრინგ ტიპის მონაცემი არის 


def stringg(listt):
    count = 0
    for char in listt:
        if type(char) == str:
            count += 1
    return count

print(stringg([345, 32, "Gamarjoba", "Kargad", 90.6, 7, 8.8, True and False, "True", "False"]))