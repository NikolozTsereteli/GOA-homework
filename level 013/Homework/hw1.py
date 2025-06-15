# 1) შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა მომხმარებლის შემოტანილი სიტყვა. ხმოვნები სადაც იქნება ! ნიშნით ჩაინაცვლოს და თანხმოვნები *-ით სხვა დანარჩენი სიმბოლო იყოს ისე როგორ იქნება. 


word = input("Enter a random word here: ")
def signs(word):
    vowels = "აეიოუ"
    consonants = "ბგდვზთკლმნპჟრსტფქღყშჩცძწჭხჯჰ"
    for i in word:
        if i in vowels:
            i = "!"
            print(i)
        elif i in consonants:
            i = "*"
            print(i)
        else:
            print(i) 
    return word  

signs(word)        
