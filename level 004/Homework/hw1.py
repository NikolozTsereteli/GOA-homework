# 1) მომხმარებელს შემოატანინე რიცხვი და მომხმარებლის შემოტანილ რიცხვამდე გამოიტანეთ ყველა რიცხვის კვადრატების ჯამი.

sum = 0
Number = int(input("Enter a number here: "))
for i in range(1, Number):
    sum += (i * i)
print(sum)


