# 6)შექმენით ფუნქცია რომელსაც გადაეცემა სია -- >["kaxi" , "ana" ,"Aleqsandre", "ia" , "Giorgi" , "Iamze" , "beqa"],თქვენი დავალებაა შეამოწმოთ თუ ამ სიიდან თითოეული ელემენტი იწყება დიდ ასოზე ანუ არის capitalize() ეს ელემენტები ადაამატოთ ახალ სიაში და დააბრუნოთ ეს ახალი სია სადაც მოთავსებული გვექნება დიდი ასოთი დაწყებული სიტყბვები


def upper_or_not(listt):
    New_list = []
    for char in listt:
        if char == char.capitalize():
            New_list.append(char)
    
    return New_list

print(upper_or_not(["kaxi" , "ana" ,"Aleqsandre", "ia" , "Giorgi" , "Iamze" , "beqa"]))
