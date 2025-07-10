# 4) შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილი რიცხვის ჩათვლით გამოგვიტანს ყველა კენტი რიცხვის კვადრატის ჯამს


num = int(input("Enter a random number here: "))
def average(num):
    sum = 0
    for i in range(1, num + 1):
        if i % 2 != 0:
            sum += i * i

    return sum

print(average(num))