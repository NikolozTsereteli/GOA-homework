# 5)შექმენით სია სადაც შეიყვანთ რიცხვებს,თქვენი დავალებაა გაიგოთ ლუწ ინდექსზე მდგომი ელემენტების ჯამი


listt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for i in range(len(listt)):
    if i % 2 == 0:
        sum += listt[i]
print(sum)

    
