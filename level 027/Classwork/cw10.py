# 11)შექმენი ფუნქცია რომელსაც გადაეცემა სტრინგები,შეამოწმე თუ სტრინგის პირველი ასო არის დიდი და მისი სიგრძე ნაკლებია 5 ზე ეს სტრინგები ჩაამატრ ახალ სიაში,შემდეგ ამ ახალ სიაში ჩამატებული ელემენტები გაფილტრეთ(sorted) მათი სიგრძის მიხედვით და ეს სია შემოატრიალეთ


def change_list(listt):
    New_list = []
    for name in listt:
        if name == name.capitalize() and len(name) < 5:
            New_list.append(name)

    return sorted(New_list, key=len, reverse=True)

print(change_list(["Nika", "Ia", "Anano", "Gela", "Ana", "Avtandili", "Keso"]))