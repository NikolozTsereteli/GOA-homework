# 3)მომხმარებელკს შემოაყვანინეთ სახელი გვარი ასაკი და მისი სიმაღლე და შეინახეთ ეს მნიშვნელობები ცვლადებში,თქვენი დავალებაა რომ მოახდინოთ ამ ოთხი მნიშვნელობის კონკატინაცია,ასევე ეს მნიშვნელობები ერთმანეთსაგან გამოყავით space ბით


Name = input("Enter your name here: ")
Surename = input("Enter your surename here: ")
Age = int(input("Enter your age here: "))
Height = float(input("Enter your height here: "))

print("My name is" + " " + Name + " " + Surename + "." + " " + "I am " + str(Age) + " " + "years old, and I am " + str(Height) + " meters tall." )