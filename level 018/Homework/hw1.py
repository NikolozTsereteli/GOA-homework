# 1)შექმენით ფუნქცია რომელსაც გადაეცემა რიცხვების სია,თქვენი დავვალებაა იპოვოთ ამ სიიდან ყველაზე პატარა და ყველაზე დიდი რიცხვები


def big_small_numbers(listt):
    min_num = listt[0]
    for i in listt:
        if i < listt[0]:
            min_num = i
    
    max_num = listt[0]
    for j in listt:
        if j > listt[0]:
            max_num = j

    return min_num, max_num
    
print(big_small_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))