# 14)შექმენი ფუნქცია რომელსაც გადაეცემა ერთმთლიანი წინადადება,ამ წინადადებაშ სიტყვები გამოყოფილები უნდა იყვნენ სპეისებთ,შენი დავლაებაა ამ სტრინგშ მოთავსებული ყველა სიტყვა გადაიყვანო სიაში(სესაბამისი ფუქნცია)


def change_string(stringg):
    New_list = []
    New_list = (stringg.split(" "))

    return New_list

print(change_string("My name is Nikoloz Tsereteli"))
