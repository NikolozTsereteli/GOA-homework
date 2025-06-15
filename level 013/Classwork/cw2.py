# 2) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა მომხმარებლის შემოტანილი სიტყვა და ამ სიტყვაში დაითვლის ასო "k'ს რაოდენობას. დააიგნოროს ქეის სენსიტიურობა.


word = (input("Enter a random word here: "))
def amount_of_k(word):
    count = 0
    for char in word:
        if char == "k" or char == "K":
            count += 1
    return count

print(amount_of_k(word))