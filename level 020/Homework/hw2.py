# 2)შექმენით ფუნქცია სადაც მოთავსებული გექნებათ რიცხვები,თქვენი დავალებაა გააარკვიოთ თ ეს რიცხვი არის ლუწი და ამავდროულად დგას ლუწ ინდექსზე, მაშინ ეს რიცხვები დაამატე ახალ სიაში და იპოვეთ ამ ახალ სიაში მყოფი რიცხვების საშუალო არითმეტიკული


def change_list(listt):
    New_list = []
    for i in range(len(listt)):
        if i % 2 == 0 and listt[i] % 2 == 0:
            New_list.append(listt[i])
    
    sum = 0
    amount = 0
    for j in New_list:
        sum += j
        amount += 1

    return sum / amount

print(change_list([2, 45, 56, 67, 76, 78, 89, 9, 17, 18, 80, 823, 48, 59, 88, 783, 240]))