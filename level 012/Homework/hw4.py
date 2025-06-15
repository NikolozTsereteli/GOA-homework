# 4) შექმენით ფუნქცია, სადაც მომხმარებლის შემოტანილ ტექსტს შეაბრუნებთ ისე რომ თითოეულ ასოს შორის - (ტირე) იყოს. (სლაისინგის გარეშე სცადეთ შებრუნება) 

# მაგ: თუ მომხმარებელმა შემოიტანა Goa შედეგი უნდა იყოს a-o-G



text = input("Enter your text here: ")
def invert(text):
    New_text = ""
    for char in text:
        if char == text[0]:
            New_text = char 
        else:
            New_text = char + "-" + New_text
    return New_text

print(invert(text))




 

        