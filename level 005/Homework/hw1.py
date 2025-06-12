# 1)მომხმარებელს შემოატანინეთ ორი რიცხვი,თქვენი დავალებააა შეადაროთ ეს ორი რიცხვი ერთმანეთს,თუ პირველი რიცხვი მეტია რიცხვზე ტერმინალში გამოიტანეთ True,თუ პირველი რიცხვი ნაკლებია მეორე რიცხვზე ტერმინალში გამოიტანე False,ყველა სხვა დანარჩენ შემთხვევაში გამოიტანე Other

Number1 = int(input("Enter your number here: "))
Number2 = int(input("Enter your number here: "))
if Number1 > Number2:
    print(True)
elif Number1 < Number2:
    print(False)
else:
    print("Other")



