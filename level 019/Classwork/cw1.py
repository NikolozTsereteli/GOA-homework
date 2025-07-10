# 1) შექმენით ფუნქცია რომელსაც გადაეცემა მომხმარებლის შემოტანილი რიცხვი. დააბრუნეთ ამ რიცხვის ჩათვლით ყველა ლუწი რიცხვის საშუალო არითმეტიკული


num = int(input("Enter a random number here: "))
def average(num):
    sum = 0
    amount = 0
    for i in range(1, num + 1):
        if i % 2 == 0:
            sum += i
            amount += 1

    return sum / amount
            
print(average(num))