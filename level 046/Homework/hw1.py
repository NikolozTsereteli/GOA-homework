def disemvowel(string_):
    new_string = ""
    vowels = "aeiouAEIOU"
    for char in string_:
        if char not in vowels:
            new_string += char
    
    return new_string

print(disemvowel("This Website is for Losers LOL!"))