# 4)მომხმარებელს შემოატანინე მისი საყვარელი ფერი,თუ საყვარელი ფერი ემთხვევა წითელს ტერმინალში გამოუტანე red is favorite color,თუ შემოტანილი ფერი ემთხვევა ყვითელს დაუპტინტე favorite color is yellow,თუ შემოტანილი ფერი ემთხვევა ლურჯს დაუპრინტე favorite color is blue,ყველა სხვა დანარჩენ შემთხვევაში დაუპტინტე other color


Your_Favorite_Color = input("Enter your favorite color: ")
if Your_Favorite_Color == "red":
    print("red is favorite color")
elif Your_Favorite_Color == "yellow":
    print("favorite color is yellow")
elif Your_Favorite_Color == "blue":
    print("favorite color is blue")
else:
    print("Other color")

