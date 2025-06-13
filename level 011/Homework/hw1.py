#  1) მომხმარებელს შეეკითხეთ ორი რიცხვი შემდეგ კი შექმენით ფუნქცია რომელსაც არგუმენტად გადასცემთ ამ ორ რიცხვს ხოლო ფუნქცია დააბრუნებს ამ ორი რიცხვის ჯამს, ასევე გააკეთე ასეთი 4 ფუნქცია სხვადასხვა მათემატიკური მოქმედებებისთვის, გამოიყენეთ პარამეტრები და არგუმენტად გადაეცით მომხარებლის შემოტანილი რიცხვები



num1 = int(input("Enter a number here: "))
num2 = int(input("Enter a number here: "))

def add_numbers(num1, num2):
    return num1 + num2

result = add_numbers(num1, num2)
print(result)



num1 = int(input("Enter a number here: "))
num2 = int(input("Enter a number here: "))

def subtract_numbers(num1, num2):
    return num1 - num2
result = subtract_numbers(num1, num2)  
print(result)  



num1 = int(input("Enter a number here: "))
num2 = int(input("Enter a number here: "))

def multiply_numbers(num1, num2):
    return num1 * num2
result = multiply_numbers(num1, num2)  
print(result)  



num1 = int(input("Enter a number here: "))
num2 = int(input("Enter a number here: "))

def divide_numbers(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("Division by zero is not allowed")

result = divide_numbers(num1, num2)  
print(result)  

