# 5) შექმენით ფუნქცია, რომელიც მომხმარებელს შემოატანინებს სახელს სანამ არ შემოიტანს თქვენს სახელს. თან ჩაამატეთ ახალ სიაში. და დააბრუნეთ ეს სია და რამდენი ელემენტისგან შედგება.


Your_name = input("Enter a random name here: ")
My_name = "Nika"
def names_list(Your_name):
    New_list = []
    while Your_name.lower() != My_name.lower():
        New_list.append(Your_name)
        Your_name = input("Enter a random name here: ")
    print(New_list)
    print(len(New_list))

    return New_list

(names_list(Your_name))
