def to_camel_case(text):
    New_list = []
    word = ""
    for char in text:
        if char in "-_":
            New_list.append(word)
            word = ""
        else:
            word += char
            
    New_list.append(word)
    result = New_list[0]
    for i in New_list[1:]:
        result += i.capitalize()
    return result

print(to_camel_case("the_stealth_warrior"))