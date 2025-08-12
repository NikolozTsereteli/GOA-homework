def calculator(txt):
    New_txt = ""
    slices = txt.split()
    if slices[1] == "+":
        New_txt = "." * (len(slices[0]) + len(slices[2]))
    elif slices[1] == "-":
        New_txt = "." * (len(slices[0]) - len(slices[2]))
    elif slices[1] == "*":
        New_txt = "." * (len(slices[0]) * len(slices[2]))
    elif slices[1] == "//":
        if len(slices[0]) > len(slices[2]):
            New_txt = "." * (len(slices[0]) // len(slices[2]))
        else:
            New_txt = ""
    
    return New_txt

print(calculator("........ + ..........."))