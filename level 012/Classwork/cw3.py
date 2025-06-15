# 3) მომხმარებელს შემოატანინეთ რიცხვი და სიის სახით დააბრუნეთ ისეთი რიცხვები რომლებიც არ იყოფა მომხმარებლის შემოტანილ რიცხვზე.


num = int(input("Enter a number here: "))
New_list = []
def non_division(num):
    for i in range(1, num):
        if num % i != 0:
            New_list.append(i)
    return New_list

print(non_division(num))        