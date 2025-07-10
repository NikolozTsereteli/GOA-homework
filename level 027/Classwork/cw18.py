# 19)შექმენი ცვლადი სადაც შეინახავ შენ პაროლს,შემდეგ მომხმარებელს შემოატანინე პაროლკსანამ მომხმარებელი სწორად არშემოიყვანს პაროლს იქამდე გაუმეორე რომ შემოიყვანოს თავიდან პაროლი


My_password = "Nika2025"
Your_password = input("Enter your password here: ")
while Your_password != My_password:
    print("Wrong password, try again!")
    Your_password = input("Enter your password here: ")
print("Nice, we got the same password!")
