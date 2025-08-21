def friend(x):
    new_x = []
    for char in x:
        if len(char) == 4:
            new_x.append(char)
    
    return new_x

print(friend(["Nika", "Luka", "Anastasia", "Giorgi", "Andria"]))