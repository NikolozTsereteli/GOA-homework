# 7)შექმენი სია სადაც გექნება ელემენტები,შენი დავალებაა ამ სიიდან ამოშალო სტრინგი მონაცემები და დააბრუნო სია სტრინგების გარეშე


New_listt = []
listt = [34, 45, 67, 78, 6456, 34.56, 0, True, False, False and True, "Nika", "Me", "IS"]
for char in listt:
    if type(char) != str:
        New_listt.append(char)
print(New_listt)
        

