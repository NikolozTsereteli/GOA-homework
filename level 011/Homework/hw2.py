# 2)  შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვებით სავსე სია ამ ფუნქციამ კი უნდა დააბრუნოს ამ სიის რიცხვების ჯამი



def add(listt):
    total = 0
    for i in listt:
        total += i
    return total

result = add([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Sum is: ", result)    