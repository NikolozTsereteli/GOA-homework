# 4) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა სია სადაც იქნება სხვადასხვა ტიპის მონაცემი. გაიგეთ ამ სიაში რიცხვების ჯამი 


def adding_numbers(listt):
    sum = 0
    for i in listt:
        if type(i) == int:
            sum += i
    return sum

print(adding_numbers([67, 54, 5, 6, "Justice", "Peace", True, 0]))
