# BONUS: შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილ რიცხვის ჩათვლით გამოგვიტანს ყველა მარტივი რიცხვის ნამრავლს. 


number = int(input("Enter your number here: "))
def multiplication(number):
    multiply = 1
    for i in range(1, number + 1):
        multiply *= i
    return multiply

print(multiplication(number))    
    

