#15)შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგების სია,თქვენი დავალებაა ამ სიაშო მყოფი სტრინგებიდან ამოშალო ხმოვნები და ახალ სიაში ჩაამატო ის თანხმოვნები რომლებიდ დარჩა,ყველას თავი მოუყარეთ ერთ სიაში მაგ --> ["ანა","გოგა"] უნდა დავაბრუნო ["ნ","გ","გ"] რადგან ხმოვნები რომ ამოვიღე მხოლოდ ეს ასოები დამრჩა


def change_list(listt):
    vowels = "aeiouAEIOU"
    New_list = []
    for name in listt:
        for char in name:
            if char not in vowels:
                New_list.append(char)

    return New_list



print(change_list(["Nika", "Ana", "Dato"]))