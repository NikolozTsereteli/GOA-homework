# 4) მომხმარებელს შემოატანინეთ ტექსტი და ამ ტექსტში დაითვალეთ რიცხვების რაოდენობა.


text = input("Enter a random text here: ")
def numbers_in(text):
    numbers = "0123456789"
    length = 0
    for char in text:
        if char in numbers:
            length += 1
    return length

print(numbers_in(text))        
            



