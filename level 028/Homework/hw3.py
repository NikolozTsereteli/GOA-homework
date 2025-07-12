# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.

# It should look like this:

# Sam Harris => S.H

# patrick feeney => P.F


def abbrev_name(name):
    New_string = ""
    for i in range(len(name)):
        if name[i] == " ":
            return name[0].upper() + "." + name[i + 1].upper()

print(abbrev_name("nikoloz tsereteli"))