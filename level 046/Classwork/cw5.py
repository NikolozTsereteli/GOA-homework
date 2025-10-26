def to_jaden_case(string):
    New_string = ""
    for char in string.split():
            New_string += char.capitalize() + " "
            
    return New_string[0 : -1]

print(to_jaden_case("dui is no joke brother"))