#12)მომხამრებელს შემოატანინეთ რიცხვი,შემდეგ შეამოწმეთ,თუ რიცხვი არის ლუწი და ასევე არის 0 ზე მეტი დაუპრინტე რომ კარგია,თუ რიცხვი არის კენტი და ასევე 0 ზე ნაკლები დაუპრინტეთ რომ ცუდია სხვა შემთხვევაში დაუპრინტეთ რომ გუდ ჯობ


Enter_number = int(input("Enter your number here: "))
if Enter_number % 2 == 0 and Enter_number > 0:
    print("Good!")
elif Enter_number % 2 != 0 and Enter_number < 0:
    print("Bad!")
else:
    print("Good job!")