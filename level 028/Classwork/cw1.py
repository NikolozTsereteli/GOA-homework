# Write a function that removes the spaces from the string, then return the resultant string.


def remove_spaces(stringg):
    stringg2 = ""
    for char in stringg:
        if char != " ":
            stringg2 += char
    return stringg2

print(remove_spaces("Nikoloz Tsereteli"))