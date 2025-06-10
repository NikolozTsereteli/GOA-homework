# 3) მომხმარებელს შემოატანინე სიტყვა და რიცხვი. ახალ ცვლადში შეინახე ყველა ამ ასოს რიცხვზე ნამრავლი. (მაგალითად რიცვად შემოიტანა 3 ტექსტად HI. შედეგი უნდა იყოს HHHIII) 

New_Word = ""
Word = input("Enter a random word here: ")
Number = int(input("Enter a random number here: "))
for i in Word:
    New_Word += i * Number
print(New_Word)

