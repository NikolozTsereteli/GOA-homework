# 22)შექმენით ფუნქცია რომელიც აბრუნებს სტრინგში ხმოვნების რაოდენობას


def count_string(stringg):
    count = 0
    vowels = "aeiouAEIOU"
    for char in stringg:
        if char in vowels:
            count += 1
    
    return count

print(count_string("Metaphysics"))



