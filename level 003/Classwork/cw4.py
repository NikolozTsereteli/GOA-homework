# 4) მომხმარებელს შემოატანინე ორი სტრინგი და for loop-ის საშუალებით დაითვალე  ორივეში სიმბოლოების რაოდენობა. შემდეგ დაპრინტეთ არის თუ არა ერთმანეთის ტოლი სიმბოლოების რაოდენობა.

count1 = 0
Stringg1 = input("Enter your text here: ")
for i in Stringg1:
    count1 += 1

count2 = 0
Stringg2 = input("Enter your text here: ")
for i in Stringg2:
    count2 += 1 
print(count1 == count2)
    
