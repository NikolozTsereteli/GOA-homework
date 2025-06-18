# 2)შექმენი ფუნქცია რომელსაც დაგაეცემა სია,შენი დავალებაა ამ სიიდან ამოშალო კენტ ინდექსზე მდგომი მხოლოდ კენტი რიცხვები და დაამატო ეს რიცხვები ახალ სიაში


def odd_numbers(listt):
    New_list = []
    for i in range(len(listt)):
        if i % 2 == 1:
            for i in listt:
                if i % 2 == 1:
                    listt.remove(i)
                    New_list.append(i)
    return New_list

print(odd_numbers([0, 1, 6, 4, 9, 5, 8, 89, 90, 9, 10, 17, 71, 14, 13, 16, 678, 0, 1, 2, 20]))