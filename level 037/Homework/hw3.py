def bonus_time(salary, bonus):
    if bonus == True:
        return "$" + str(salary * 10)
    else:
        return "$" + str(salary)
    
print(bonus_time(123000, True))