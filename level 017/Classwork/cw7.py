# 7)შექმენით ფუნქცია რომელსაც გადაეცემა შემდეგი სია["kaxi" , 5 ,"Aleqsandre", 10, "Giorgi" ,20 , "beqa"] თვენი დავალებაა ამ სიიდან ამოშალოთ მხოლოდ integer ები და დააბრუნოთ სია მათ გარეშე


def no_integers(listt):
    for char in listt:
        if type(char) == int:
            listt.remove(char)
    
    return listt

print(no_integers(["kaxi" , 5 ,"Aleqsandre", 10, "Giorgi" ,20 , "beqa"]))