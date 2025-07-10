# 2)შექმენით ფუნქცია რომელსაც გადაეცემა სახელები,ზოგი სახელი უნდა იყოს დაწყებული დიდი ასოთი ზოგი კი ჩვეულებრივ პატარა ასოებით უნდა იყოს დაწყებული,თქვენი დავალებაა ახალ სიაშ დაამატოთ მხოლოდ ის სახაელები რომელთა პირველი ასოც არის დიდი


def change_list(listt):
    New_list = []
    for char in listt:
        if char.capitalize() == char:
            New_list.append(char)

    return New_list
 
print(change_list(["Gocha", "Nukri", "Akaki", "zurabi", "gigi", "ana", "nika", "Temuka"]))