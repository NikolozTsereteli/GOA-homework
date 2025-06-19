# 6) მომხმარებელს შემოატანინეთ რიცხვი. შემდეგ სიტყვა სანამ არ შემოიტანს 'გაჩერდი!', ეგ ყველაფერი დაამატეთ ახალ სიაში და ამ სიიდან მომხმარებლის შემოტანილი რიცხვი რაც არის, იმაზე მდგომი სიტყვის ჩათვლით გამოიტანეთ ამ სიიდან სიტყვები. 


num = int(input("Enter a random number here: "))
word = input("Enter a random word here: ")
def mixed_list(num, word):
    New_list = []
    result = ""
    while word != "გაჩერდი":
        New_list.append(word)
        word = input("Enter a random word here: ")
    result = " ".join(New_list[0:num])
    print(result)
        
    return New_list

mixed_list(num, word)
        



