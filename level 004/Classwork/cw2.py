#  2) მომხმარებელს შემოატანინე პაროლი მანამ სანამ ამ პაროლის მნიშვნელობა არ იქნება 'GOA BEST' და თუ შემოიტანა პაროლი სწორად, დაპრინტე 'ყოჩაღ, პაროლი სწორია'


Password = input("Write your password here: ")

while Password != "GOA BEST":
    print("Try again") 
    Password = input("Enter your password here: ")
print("ყოჩაღ, პაროლი სწორია")
    