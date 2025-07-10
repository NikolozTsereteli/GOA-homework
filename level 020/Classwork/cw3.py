# 3)შექმენით ფუნქცია რომელსაც გადაეცემა სახელები,ეს სახელები ზოგი მთლინად უნდა იყოს დიდი ასოებით დაწერილი ზოგი კი პატარა,თქვენი დავალებაა ახალ სიაშ დაამატოთ მხოლოდ დიდი ასოებით დაწერილი სახელები


def change_list(listt):
    New_list = []
    for char in listt:
        if char.upper() == char:
            New_list.append(char)
    
    return New_list

print(change_list(["NIKA", "dato", "andria", "LASHA", "ANANO", "VAXO", "vato", "gurami"]))