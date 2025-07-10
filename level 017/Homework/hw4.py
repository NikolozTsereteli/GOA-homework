# 4. შექმენით ფუნქცია, რომელსაც გადაეცემა სია, თქვენი დავალებაა გამოიტანოთ ყველაზე დიდი რიცხვი. (max ფუნქცია არ გამოიყენოთ)


def max_number(listt):
    max_num = 0
    for i in listt:
        if i > listt[0]:
            max_num = i
    
    return max_num
        
print(max_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))