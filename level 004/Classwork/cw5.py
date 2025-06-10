# 5) მომხმარებელს შემოატანინე სახელი და ასაკი მანამ სანამ ასაკი არ იქნება თქვენი ასაკის ტოლი და სახელი არ იქნება თქვენი სახელის ტოლი


Name = input("Enter your name here: ")
Age = int(input("Enter your age here: "))
My_Name = "Nika"
My_Age = 19
while Name != My_Name or Age != My_Age:
    print("Oops! An error occured, please try again.")
    Name = input("Enter your name here: ")
    Age = int(input("Enter a number here: "))
print("Nice! We are both named " + Name + " and we are both " + str(Age) + " years old! What a coincidence!")