# 12)შექმენი სია სადაც გექნება სტრინგები და რიცხვები,რიცხვებიგადაიტანე ახალ სიაში და დაალაგე ზრდის მიხევდით სტრინგებიც ჩაამატე სხვა ახალ სიაში და ეს სტრინგების სია დააალაგეთ ანბანის მიხევდით


Numbers_list = []
Strings_list = []
listt = ["Nika", 67, 45, 34, "Dato", "Maia"]
for char in listt:
    if type(char) == int:
        Numbers_list.append(char)
    else:
        Strings_list.append(char)
    

print(sorted(Numbers_list))
print(sorted(Strings_list))



