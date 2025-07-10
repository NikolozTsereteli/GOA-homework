# 5)შექმენი ფუნქცია რომელსაც გადაეცემა ერთი მთლიანი დიდის ტრინგი,ამ სტრინგშ სიტყვები დააშორე % ამ ნიშნით,შენი დავლებაა ეს სტრინგი აქციო სიად,შემდეგ შეამოწმო თუ ამ სიაში მყოფი ელემენტი დგას ლუწ ინდექსზე ჩაამატე ახალ სიაში,შემდეგ თქვენი დავალება იქნება რომ ეს სია გადაიყვანოთ ისევ სტრინგში და ეს სიტყვები გამოყო ერთმანეთსგან სფეისებით


def list_to_string(stringg):
    words = stringg.split("%")
    even_words = []
    for i in range(len(words)):
        if i % 2 == 0:
            even_words.append(words[i])
    New_string = " ".join(even_words)

    return New_string

print(list_to_string("I%am%a%human%being,%my%name%is%Nikoloz%Tsereteli%and%I%am%19%years%old"))