# 7)მომხმარებელს შემოატანინე 50 ზე მაღალი რიცხვი for loop გამოყენებით ერთიდან მომხმარებლის შემოტანილ რიცხვამდეე დაბეჭდეთ ყველა რიცხვი 5 step ის გამოყენებით,იგივე გაააკეთეთ while loop ითაც


Enter_Higher_Then_50 = int(input("Enter a number higher then 50 here: "))
for i in range(1, Enter_Higher_Then_50, 5):
    print(i)



Enter_Higher_Then_50 = int(input("Enter a number higher then 50 here: "))
i = 1
step = 5
while i < Enter_Higher_Then_50:
    print(i)
    i += step
    
    



