# 1. შექმენით ფუნქცია, რომელიც მომხმარებლის შემოტანილ სიტყვაში დაითვლის რამდენი განსხვავებული ასოსგან შედგება ეს სიტყვა.


name = input("Enter your name here: ")
def amount_of_letters(name):
    count = 0
    num = 0
    for char in name:
        if name[num] != char in name[1:]:
            count += 1
            num += 1

    return count

print(amount_of_letters(name))