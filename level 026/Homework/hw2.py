# 2)შექმენი სია სადაც მოცემუილი იქნება სახელები თქვენი დავალებაა დაასორტიროთ ეს სახელები ანბანის მიხედვით და თან შემოატრიალოთ


def sort_list(listt):
    New_list = sorted(listt, reverse=True)
    
    return New_list

print(sort_list(["nika", "manana", "gela", "lasha", "andria", "goga"]))