# 3) მომხმარებელს შემოატანინეთ სიტყვა და for / while loop-ების საშუალებით გამოიტანეთ თითოეული ასო


name1 = input("Enter your name here: ")
for char in name1:
    print(char)


name2 = input("Enter your name here: ")
i = 0
while i < len(name2):
    print(name2[i])
    i += 1
