# 1) შექმენით ფუნქცია რომელიც შეამოწმებს არგუმენტად გადაცემულ სტრინგში თუ არის რიცხვი.


def string_with_number(stringg):
    string_num = "0123456789"
    for char in stringg:
        if char in string_num:
            print("A number or numbers are in this string")
            return
    print("There are no numbers in this string")

(string_with_number("Nikoloz Wereteli6"))
