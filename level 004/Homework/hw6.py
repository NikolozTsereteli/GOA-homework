# 6) მომხმარებელს შემოატანინე რიცხვი და ამ რიცხვის ჩათვლით ყველა რიცხვი შეკრიბე და ეს ჯამი დაპრინტე.


Number = int(input("Enter a number here:"))
i = 1
sum = 0
while i <= Number:
    sum += i
    i += 1

print("ჯამი არის: " + str(sum))