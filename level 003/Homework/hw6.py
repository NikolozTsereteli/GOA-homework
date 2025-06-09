# 6) მომხმარებელს შემოატანინეთ რიცხვი და დაპრინტე ამ რიცხვის ჩათვლით ყველაფრის ჯამი.

sum = 0
number = int(input("Enter your number here: "))
for i in range(number + 1):
    sum += i
print(sum)