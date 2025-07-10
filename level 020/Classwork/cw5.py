# 5)შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგებით სავსე სია,თქვენი დავალებაა ახალ სიაში დაამატოთ მხოლოდ ის სტრინგები რომლებიც იწყებიან დიდ ასოზე და ასევე მათ სიგრძე არის 5 ზე ნაკლები და ასევე ამ სტრინგში არის ერთი ასო მაინც ხმოვანი


def create_new_list(listt):
    New_list = []
    vowels = "aeiou"
    for word in listt:
        if word[0] == word[0].upper() and len(word) < 5:
            for char in word:
                if char in vowels:
                    New_list.append(word)
                    break

    return New_list

print(create_new_list(["Random", "Specific", "intentional", "radiation", "huh", "cat", "Dog", "Nice"]))