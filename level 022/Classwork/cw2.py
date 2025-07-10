# 2)მომხმარებელს შემოატანინეთ რაიმე რიცხვი,სანამ მომხმარებელი არ შემოიყვანს 10 ზე ნაკლებ რიცხვს გაუმეორეთ რომ თავიდან შემოიტანოს,თან არასწორად შემოყვანილი მნიშნველობები ჩაამატეთ სიაში


num = int(input("Enter a random number here: "))
New_list = []
while num >= 10:
    New_list.append(num)
    print("Try again")
    num = int(input("Enter a random number here: "))
    
print(New_list)
    



