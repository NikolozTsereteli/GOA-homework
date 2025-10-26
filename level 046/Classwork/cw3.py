def square_digits(num):
    num2 = ""
    for i in str(num):
        num2 += str(int(i)**2)
    
    return int(num2)

print(square_digits(9119911991199119911991199119911991199119911991199119911991199119))
