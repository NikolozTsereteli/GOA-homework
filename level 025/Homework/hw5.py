# 5) შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილ წინადადებაში ხმოვან ასოებს გაფილტრავს.


def change_list(stringg):
    New_string = ""
    vowels = "aeiouAEIOU"
    for char in stringg:
        if char not in vowels:
            New_string += char

    return New_string

print(change_list("My name is Nikoloz Tsereteli"))