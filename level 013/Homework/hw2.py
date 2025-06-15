# 2) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა მომხმარებლის სახელი და ასაკი. შეამოწმეთ თუ ასაკი მეტი არის 18-ზე და მისი სახელი არის თქვენი სახელის ტოლი მაშინ დააბრუნოს თქვენ წარმატებით აიღეთ მართვის მოწმობა. სხვა დანარჩენ შემთხვევაში რომ ჩაიჭრნენ


Your_name = input("Enter your name here: ")
Age = int(input("Enter your age here: "))
My_Name = "Nika"
def driving_license(Your_name, Age):
    if Age > 18 and Your_name == My_Name:
        print("You successfully got your driver's license!")
    else: 
        print("You failed.")
    return Your_name, Age
driving_license(Your_name, Age)

