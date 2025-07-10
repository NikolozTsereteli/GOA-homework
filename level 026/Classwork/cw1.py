# 1)შექმენი სია,სადაც მოათავსებთ სახელებს,თქვენი დავალებაა დაასორტიროთ ეს სია სიაში მტოფი სახელების სიგრძის მიხედვით და შემოატრიალოთ უკუღმა


def change_list(listt):
    New_list = sorted(listt, key=len, reverse=True)
    
    return New_list

print(change_list(["Nika", "Maia", "Zura", "Ana", "Akaki", "Ilia", "Andria", "Vaxo"]))