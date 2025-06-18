# 4) შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილ სტრინგს დაფარავს *-


text = input("Enter a string here: ")
def change(text):
    New_text = ""
    for char in range(len(text)):
        char = "*"
        New_text += char
    return New_text

print(change(text))





