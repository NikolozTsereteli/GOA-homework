# Bonus:
# • შექმენით ფუნქცია სადაც მომხმარებლის შემოტანილი რიცხვის გამყოფების ჯამს დაგვიბრუნებს. 


num = int(input("Enter your number here: "))
def summ(num):
    sum = 0
    for i in range(1, num + 1):
        if num % i == 0:
            sum += i
    return sum

print(summ(num))
