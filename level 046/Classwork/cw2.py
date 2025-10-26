# 2)შექმენით სია რომელსაც გადაეცემა  სახელი და გვარები მაგ --> ["გოგა ჩალაური" , "ანდრია შანავა" , "დათო მირიბიანი"] , თქვენი დავალებაა რომ ამ სიაში მყოფი ე;ემენტების სახელები მოათავსოთ სიაში რომელსაც ერქმევა names და გვარები მოათავსოთ სხვა სიაში რომელსაც ერქმევა surnames


listt = ["გოგა ჩალაური" , "ანდრია შანავა" , "დათო მირიბიანი"]
names = []
surenames = []
New_string = " ".join(listt)
New_list = New_string.split()
for i in range(len(New_list)):
    if i % 2 == 0:
        names.append(New_list[i])
    else:
        surenames.append(New_list[i])

print(names)
print(surenames)
