# 4)შექმენი ფუნქცია რომელსაც გადაეცემა სია,შენი დავალებაა შეამოწმო თუ ამ სიაში მყოფი სახელების სიმბოლოები დგანან კენტ ინდექსზე და ასევე არიან lowercase ები,ჩაამატო ერთ მთლიან სიაში ასეთი ასოები


def change_list(listt):
    New_list = []
    for name in listt:
        for i in range(len(name)):
            if i % 2 != 0 and name[i] == name[i].lower():
                New_list.append(name[i])

    return New_list

print(change_list(["Nika", "Goga", "Nato", "Ana", "anano", "nanuli"]))