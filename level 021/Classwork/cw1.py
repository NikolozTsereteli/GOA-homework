# 1) მომხმარებელს შემოატანინეთ სიტყვა მანამ სანამ არ შემოიტანს მინიმუმ 6 ნიშნას.


name = input("Enter a random name here: ")
while len(name) < 6:
    print("Try again")
    name = input("Enter a random name here: ")
print("Nice name!")

