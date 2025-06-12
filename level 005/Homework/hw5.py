# 5)მომხმარებელს შემოატანინე რიცხვი,for loop ის გამოყენებით გამოიტანე თითოეული რიცხვი ერთიდან ამ რიცხვამდე,იგივე გააკეთეთ While loop-


Number = int(input("Enter a number here: "))
for i in range(1, Number):
    print(i)


Number = int(input("Enter a number here: "))
i = 1
while i < Number:
    print(i)
    i += 1
