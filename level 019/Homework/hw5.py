# 5) შექმენით ფუნქცია რომელიც მომხმარებელს შემოტანილ სიტყვიდან ლიწ ინდექსზე მდგომ სიმბოლოების გაერთიანებას დაგვიბრუნებს


name = input("Enter your name here: ")
def change_string(name):
    New_string = ""
    for i in range(len(name)):
        if i % 2 == 0:
            New_string += name[i]

    return New_string

print(change_string(name))