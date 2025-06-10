# BONUS:
# 11) მომხმარებელს შემოატანინეთ სტრინგი და for loop-ის საშუალებით შეაბრუნეთ ეს სტრინგი. შემდეგ გაარკვიეთ არის თუ არა პალინდრომე. (for loop-ით შემოატრიალეთ  და პალინდრომე არის ისეთი სიტყვა რომლის საწყისი ვერსიაც ემთვევა შებრუნებულს) 


Stringg = input("Enter your string here: ")
Backwards_Stringg = ""
for i in Stringg:
    Backwards_Stringg = i + Backwards_Stringg

if Stringg == Backwards_Stringg:
    print("ეს არის პალინდრომი")
else:
    print("ეს არ არის პალინდრომი")    

