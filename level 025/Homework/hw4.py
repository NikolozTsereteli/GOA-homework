# 4) შექმენით სია რომელიც სტრინგებით იქნება სავსე. გადაუარეთ ამ სიას და თითოეული ელემენტის კენტ ინდექსზე მყოფი სიმბოლოები გაერთიანეთ და ისე ჩაამატეთ ახალ სიაში.


def change_list(listt):
    New_list = []
    for name in listt:
        for i in range (len(name)):
            if i % 2 == 1:
                New_list.append(name[i])

    return New_list

print(change_list(["Nika", "Maia", "Keso", "Andria", "Gabrieli", "Avtandili"]))