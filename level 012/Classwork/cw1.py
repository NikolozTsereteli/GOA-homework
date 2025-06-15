# 1) შექმენით ფუნქცია, სადაც მოხმარებელს შემოატანინებთ რიცხვს და ამ რიცხვის გამყოფებს დააბრუნებს სიაში.


num = int(input("Enter your number here: "))
New_list = []
def listt(num):
    for i in range(1, num + 1):
        if num % i == 0:
            New_list.append(i)
    return New_list

print(listt(num))
