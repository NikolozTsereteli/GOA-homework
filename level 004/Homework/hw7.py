# 7) მომხმარებელს შემოატანინე პაროლი. და ჰქონდეს სამი ცდა


Password = ""
iteration = 0

while len(Password) < 10 and iteration < 3:
    Password = input("Enter your password here: ")

    if len(Password) < 10:
        print("Try again")
        iteration += 1
    

if len(Password) >= 10:
    print("Password entered successfully")
    
else:
    print("Your limit of invalid passwords are up")

    
