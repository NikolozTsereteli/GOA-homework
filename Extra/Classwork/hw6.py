# 6)შექმენი ფუნქცია რომელსაც გადაეცემა სტრინგი --> "my name is goga", თქვენი დავალებაა ამ სტრინგში თითოეული სიტყვის  პირველი ასო გაადიდოთ და დააბრუნოთ ისევ სტრინგის სახით --> "My Name Is Goga"


def change_string(stringg):
    New_list = stringg.split(" ")
    New_list2 = []
    for word in New_list:
        New_list2.append(word.capitalize())

    New_string = " ".join(New_list2)
    return New_string
        
print(change_string("my name is goga"))