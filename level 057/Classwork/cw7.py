def position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return "Position of alphabet: " + str(alphabet.index(letter) + 1)

print(position("z"))