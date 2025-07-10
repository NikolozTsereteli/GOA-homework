# 4) შექმენით ფუნქცია რომელიც შეამბრუნებს მომხმარებლის შემოტანილ სიტყვას


word = input("Enter a random word here: ")
def reverse_string(word):
    New_string = ""
    New_string += word[-1::-1]
    
    return New_string

print(reverse_string(word))