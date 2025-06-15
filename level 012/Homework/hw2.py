# 2) შექმენით ფუნქცია რომელსაც გადაეცემა სია, ამ სიში უნდა იყოს ყველა ტიპის მონაცემი. დააბრუნეთ ინტეჯეტ ტიპის ელემენტები ახალ სიაში.


def get_integers(listt):
    New_list = []
    for char in listt:
        if type(char) == int:
            New_list.append(char)
    return (New_list)
                
    
    

print(get_integers([23, 45, 56, 56657.34535, 46, 34.6, 6.6, "Nika", "dato", "SHALVA", True and False, False and True]))