# 1)შექმენით ფუნქცია რომელსაც გადაეცრმა რიცხვებით სავსე სია,თქვენი დავალებაა ამ სიიდან ამოიღოთ მხოლოდ ლუწი რიცხვები  ჩაამატო ახალ დიაში და დაალაგო ასევე ზრდის მიხედვიტ


def change_list(listt):
    New_list = []
    for i in listt:
        if i % 2 == 0:
            New_list.append(i)

    return sorted(New_list)

print(change_list([2, 3, 1, 5, 67, 43, 78]))