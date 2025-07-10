# 1)შექმენით ფუნქცია რომელიც შეამოწმებს არის თუ არა გადმოცემულ სტრინგში ხმოვნები,თუ არის დააბრუნე ეს ხმოვნები ასევე  დაითვალე რამდენი ხმოვანი იყო მოცემულ სტრინგში


def count_vowels(stringg):
    vowels = "aeiouAEIOU"
    amount = 0
    for char in stringg:
        if char in vowels:
            print(char)
            amount += 1
        
    return amount
        
print(count_vowels("Maia Tsereteli16"))

