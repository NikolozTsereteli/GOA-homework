# 21)დაწერეთ ფუნქცია, რომელიც for ციკლის გამოყენებით ითვლის მასივში რამდენი ელემენტია 10-ზე მეტი.


def count_list(listt):
    count = 0
    for i in listt:
        if i > 10:
            count += 1
    
    return count

print(count_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17]))