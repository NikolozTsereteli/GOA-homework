# 2)შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგი -- > "ჰიდროელექტროსადგური" და რიცხვი პარამეტრად,თქვენი დავალებააა დააბრუნოთ ეს სტრინგი 0 დან იმ ინდექსმდე რა რიცხვსაც შემოიტანს მომხმარებელი


num = int(input("Enter a random number here: "))
def return_string(stringg, num):
    New_string = ""
    for i in range(num):
            New_string += stringg[i]
    return New_string
            
print(return_string("ჰიდროელექტროსადგური", num))






