# 3) შექმენით ფუნქცია რომელსაც გადაეცემა მომხმარებლის შემოტანილი სახელი. იმ შემთხვევაში თუ თქვენი სახელები ემთხვევა ქეის სენსიტიურობის დაიგნორების შემთხვევაშიც, მაშინ დააბრუნოს: გამარჯობა {სახელი}!, სასიამოვნოა თქვენი გაცნობა. სხვა შემთხვევაში გამარჯობა {სახელი}! 


Your_name = input("Enter your name here: ")
My_name = "Nika"
def same_names(Your_name):
    if Your_name.lower() == My_name.lower():
        print("გამარჯობა " + Your_name + "! სასიამოვნოა თქვენი გაცნობა.")
    else:
        print("გამარჯობა " +  Your_name) 

    return Your_name

print(same_names(Your_name))