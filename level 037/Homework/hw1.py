def to_alternating_case(string):
    New_string = ""
    for i in string:
        if i == i.lower():
            New_string += i.upper()
        else:
            New_string += i.lower()

    return New_string

print(to_alternating_case("HeLlO WoRLd"))