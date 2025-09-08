# 3)შექმენი ცვლადი სადაც შეინახავთ პაროლს,შემდეგ მომხმარებეელს შემოატანინე რაიმე პაროლი,სანამ მომხ შემოტანილი პაროლი არ დაემთხვევა ენს პაროლს იქამდე მოსთხოვე თაავიდან შემოტანა,თუ სწორად შემოიყვანა პაროლი მაშინ დაუპრინტე რომ სწორი ხარ


My_password = "NikolozTsereteli"
Your_password = input("Enter your password here: ")
while Your_password != My_password:
    print("Wrong password, try again!")
    Your_password = input("Enter your password here: ")
print("You entered the correct password!")
