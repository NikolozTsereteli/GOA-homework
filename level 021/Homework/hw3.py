# 3) შექმენით ფუნქცია რომელიც შეამოწმებს არის თუ არა არგუმენტად გადაცემულ სტრინგში ერთი დიდი ასო მაინც


def upper_or_lower(stringg):
    for char in stringg:
        if char == char.upper():
            print("There is an uppercase letter in this string")
            break

    else:
        print("There are no uppercase letters in this string")

    return stringg

(upper_or_lower("Sanctification"))