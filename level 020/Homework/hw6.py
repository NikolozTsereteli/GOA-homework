# 6)მომხმარებელს შემოატანინეთ სახელი და WHILE LOOP ის დახმარებით ამ სტრინგიდან გამოიტანეთ ყოველი მეორე ასო,იგივე FOR LOOP ითაც გააკეთეთ


name1 = input("Enter your name here: ")
for i in range(len(name1)):
    if i % 2 != 0:
        print(name1[i])

name2 = input("Enter your name here: ")
i = 0
while i < len(name2):
    print(name2[i])
    i += 1