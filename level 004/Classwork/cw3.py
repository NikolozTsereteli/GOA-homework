# 3) მომხმარებელს შემოატანინე რიცხვი და მანამ სანამ ეს რიცხვი არ იქნება 16-ის ტოლი მაქამდე შემოატანინეთ რიცხვი თავიდან


Number = int(input("Enter a number here: "))
while Number != 16:
    print("Try again")
    Number = int(input("Enter a number here: "))
print("You guessed the right number, congrats!")