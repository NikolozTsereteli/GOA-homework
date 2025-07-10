# 3)შექმენი ფუნქცია რომელსაც გადაეცემა სხვადასხვა მონაცემთა ტიპები,შენი დავლებაა სიიდან ამოიღო მხოლოდ სტრინგ ტიპის მონაცემები რომლების სიგრძეც არის ნაკლები 5 ზე და იწყება დიდი ასოთი და დაამატო ახალ სიაში,შემდეგ ეს სია დაასორტირე სიგრძის მიხედვით და შემოატრიალეთ


def change_list(listt):
    New_List = []
    for char in listt:
        if type(char) == str and len(char) < 5 and char == char.capitalize():
            New_List.append(char)
    reverse_list = sorted(New_List, key=len, reverse=True)
    
    return reverse_list
            
print(change_list([23, 45.6, 5.6, "Science", "History", False, "Mathematics", "Physics", "Metaphysics", True, "Me", "You", "Us", "him", "them"]))