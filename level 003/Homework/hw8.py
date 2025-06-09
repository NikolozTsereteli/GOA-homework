# 8) მომხმარებელს შემოატანინეთ ტექსტი და დაითვალეთ ამ ტექსტში სიმბოლოების რაოდენობა.


text = input("Enter random text here: ")
count = 0
for i in text:
    count += 1
print("სიმბოლოების რაოდენობაა:", count)