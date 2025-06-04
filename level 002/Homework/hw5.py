# 5) მომხმარებელს შემოატანინე სახელი. რასაც შემოიტანს მომხმარებელი ეგ გაამრავლე 5-ზე (ანუ დავუშვათ შემოიტანა d მაშინ ddddd რომ მიიღოთ) შეინახე ახალ ცვლადში და შემდეგ შეამოწმე ამ ახალი ცვლადის მნიშვნელობა სტრინგი არის თუ ინტეჯერი. (or ოპერატორი გამოიყენეთ)

Name = input("Come on, write your name right here: ")
Name1 = Name * 5
if type(Name1) == str or type(Name1) == int:
    print("The new veriable is either a string or an intiger.")

if type(Name1) == str:
    print("It is a string.")
elif type(Name1) == int:
    print("It is an intiger.")
