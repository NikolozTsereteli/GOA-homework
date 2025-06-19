# 4) შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილ სიტყვას ასო a-ზე გახლიჩავს და დააბრუნეთ სიის სახით.


word = input("Enter a random word here: ")
def word_to_list(word):
    New_list = []
    New_list = word.split("a")

    return New_list

print(word_to_list(word))

