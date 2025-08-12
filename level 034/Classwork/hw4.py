# 4)შექმენით ფუნქცია რომელსაც გადაეცემა სია სადაც მოთავსებული იქნება როგორც სტრინგები ასევე ინტეჯერები,თქვენი დავალებაა სტრინგ ტიპის მონაცემები ჩაამატო ახალ შექმნილ სიაში და დაასორტირო ანბანის მიხედვით,ხოლო ინტეჯერებიც ჩაამატე სხვა ახალ სიაში და ეს საბოლოო სიაც დაასორტირე თან შემოატრიალე


def change_lists(listt):
    Integer_list = []
    String_list = []
    for i in listt:
        if type(i) == int:
            Integer_list.append(i)
        else:
            String_list.append(i)

    return sorted(String_list), sorted(Integer_list, reverse= True)


print(change_lists(["Nika", 6, "Dato", 67, "Ana", 6778, "Keso", 55454, 9]))