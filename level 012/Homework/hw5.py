# 5) შექმენით ფუნქცია სადაც მომხმარებელს შემოატანინებს სიტყვას და მანამ უნდა შემოატანინოთ სანამ არ შემოიტანს “საკმარისია”. ყველა შემოტანილი სიტყვა დაამატეთ ახალ სიაში და ეს სია დააბრუნეთ.


word = input("Enter a random word here: ")
def listt(word):
    New_list = []
    while word != "საკმარისია":
        print("Try again")
        New_list.append(word)
        word = input("Enter a random word here: ")
    return New_list

print(listt(word))
    
