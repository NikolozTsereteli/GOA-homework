# 6)მომხმარებელს შემოატანინე ათზე მაღალი რიცხვი,for loop ის გამოყენებით იპოვეთ 5 დან მომხმარებლის შემოტანილ რიცხვამდე ყველა რიცხვის ჯამი,იგივე გააკეთეთ while loop ითაც


Enter_Higher_Then_10 = int(input("Enter a number higher then 10 here: "))
sum = 0
for i in range(5, Enter_Higher_Then_10):
    sum += i
print(sum)



Enter_Higher_Then_10 = int(input("Enter a number higher then 10 here: "))
i = 5
sum = 0
while i < Enter_Higher_Then_10:
    sum += i
    i += 1
print(sum)