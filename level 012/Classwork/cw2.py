# 2) შექმენით ფუნქცია, რომესლაც გადაეცემა მომხმარებლის შემოტანილი ტექსტი და დაითვლით ასო 'a'-ს რაოდენობას. (დიდადაც რომ იყოს დაწერილი ისიც რომ ჩაითვალოს). 


text = input("Enter a random text here: ")
def stringg(text):
    length = 0
    for i in text:
        if i == "a" or i == "A":
            length += 1
    return length

print(stringg(text))        

