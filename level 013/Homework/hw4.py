# 4) შექმენით ფუნქცია რომელიც მომხმარებელს შემოატანინებს სიტყვას მანამ სანამ არ შემოიტანს 'საკმარისია'ს. ეს შემოტანილი სიტყვები დაამატეთ სიაში და გაფილტრეთ. სიაში უნდა იყოს ისეთი სიტყვები რომლის სიგრძეც არ აღემატება 5-ს და ურევია რიცხვები.


word = input("Enter a random word here: ")
def filtered_list(word):
    New_list = []
    numbers = "0123456789"
    while word != "საკმარისია":
        print("Try again")
        New_list.append(word)
        word = input("Enter a random word here: ")
    Filtered = []
    for word in New_list:
        if len(word) > 5:    
            for char in word:
                if char in numbers:
                    Filtered.append(word)
                    break
        

    return Filtered

print(filtered_list(word))


            
            
    
    
    