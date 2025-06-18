# 5) შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილ რიცხვს დაშლის მამრავლებად. მაგალითად ასე => თუ შემოიტანა რიცხვი 1980 მაშინ შედეგი იყოს 1000 + 900 + 80 (მარტო 1980-ზე არ განიხილოთ ეგ, მაგალითად მოვიყვანე რომ მიხვდეთ !)


num = int(input("Enter a number here: "))
def multiples(num):
    if num <= 10:
        print(num)
    elif num > 10 and num < 100:
        num1 = num - int(str(num)[1]) 
        print(str(num1) + " + " + str(int(str(num)[1])))
    elif num > 100 and num < 1000:
        num2 = num - int(str(num)[1::])
        print(str(num2) + " + " + str(int(str(num)[1])) + "0" + " + " + str(int(str(num)[2])))
    elif num > 1000 and num < 10000:
        num3 = num - int(str(num)[1::])
        print(str(num3) + " + " + str(int(str(num)[1])) + "00" + " + " + str(int(str(num)[2])) + "0" + " + " + str(int(str(num)[3])))

    return num

multiples(num)

