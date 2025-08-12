# 3)შექმენი სია სადაც გექნებათ მოცემული სტრინგები,შენი დავალებაა დააბრუნო სია სადაც ეს სტრინგები დალაგებულები იქნებიან სიგრძის მიხედვით და თან შემოატრიალეთ ეს სია,გამოიყენეთ შესაბამისი ფუნქცია

New_list = []
string_list = ["Nika", "Daviti", "Mariami", "Ana"]
New_list = sorted(string_list, key = len, reverse= True)
print(New_list)