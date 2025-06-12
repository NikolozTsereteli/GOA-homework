# 3)შექმენი ორი ცვლადი ერთში შეინახე შენი სახელი მეორეში შენი ასაკი,შენი დავალებაა შეამოწმო,თუ ასაკი მეტია 18ზე ამ შემთხვევის შიგნით უნდა შეამოწმო შემდეგი პირობა,თუ სახელი ემთხვევა შენს სახელს დაუპრინტე we have same names and we are adults,სხვა შემთხვევაში კი დაუპრინტე we dot have same names but we are adults,ბოლოს დავუბრუნდეთ ასაკს და შევამოწმოთ თუ ასაკი ნაკლებია 18ზე დაპრინტეთ we dont have same names and we are not adults

Your_Name = input("Enter your name here: ")
My_Name = "Nika"
My_Age = 19

if My_Age > 18 and Your_Name == My_Name:
    print("We have the same names and we are adults")
elif My_Age > 18 and Your_Name != My_Name:
    print("We don't have the same names but we are adults")
else:
    print("We don't have the same names and we are not adults")

