# 1) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა მომხმარებლის შემოტანილი სიტყვა და დაითვლის სიგრძეს  len() ფუნქციის გარეშე.


word = input("Enter a random word here: ")
def calculate_length(word):
    length = 0
    for char in word:
        length += 1
    return length

print(calculate_length(word))

