#4)შემოატანინეთ მომხმარებელს თავისი სახელი:
# თუ სახელი უდრის admin:
# მოთხოვეთ შემოიყვანოს ადმინის პაროლი:
# თუ პაროლი უდრის adminpassword123:
# დაპრინტეთ სალამი ადმინ
# სხვა შემთხვევაში:
# დაპრინტეთ წვდომა არ გაქვს
# სხვა შემთხვევაში:
# დაპრინტეთ სალამი მომხმარებელო


Your_name = input("Enter your name here: ")
if Your_name == "admin":
    print("Please enter admins password")
    Admin_password = input("Enter admins password here: ")
    if Admin_password == "adminpassword123":
        print("Hello Admin!")
    else:
        print("You don't have access.")
else:
    print("Hello user!")

