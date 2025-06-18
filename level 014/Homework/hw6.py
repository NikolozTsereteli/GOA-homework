# Bonus: 
# შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილ სტრინგში ლუწ ინდექსზე მდომ სიმბოლოებს დაგვიბრუნებს.


text = input("Enter a random word here: ")
def even_index(text):
    New_string = ""
    for i in range(len(text)):
        if i % 2 == 0:
            New_string += text[i]
    
    return New_string

print(even_index(text))
        
