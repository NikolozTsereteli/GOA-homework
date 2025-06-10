# 2) მომხმარებელს შემოატანინე რიცხვი და მომხმარებლის შემოტანილი რიცხვიდან ამ რიცხვის კვადრატის ჩათვლით გამოიტანეთ ყველა რიცხვის ჯამი


sum = 0
Number = int(input("Enter your number here: "))
for i in range(Number, Number * Number + 1):
    sum += i
print(sum)
   

