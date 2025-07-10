# 2) შექმენით ფუნქცია რომელიც შეაბრუნებს სიის ელემენტებს, (for loop-ით)


def reverse(listt):
    New_list = []
    for i in range(len(listt)):
        New_list.append(listt[-1::-1])
    
    return New_list

print(reverse(["Heresy", "Vatican 2", "Nuvos Ordo", "Nostra Aetate", "Lumen Gentium"]))