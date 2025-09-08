def xo(s):
    new = s.lower()
    return new.count("x") == new.count("o")

print(xo("xxoOm"))