# 4) შექმენით ფუნქცია რომელსაც გადაეცემა წინადადება,თქვენი დავალებაა ამ წინადადებაში მყოფი სიტყვები წარმოაგგინოთ სიის სახით(გამოიყენეთ შესაბამისი ფუნქცია),შემდეგ ამ სიას გადაუარეთ და შეამოწმეთ,თუ ამ სიაშიმოცემულუ სიტყვის სიგრძე ნაკლებიაა 5 ზე,დაპრინტეთ ნაკლებია 5 ზე,სხვა შემთხვევაში დაპრინტეთ მეტია 5 ზე


def change_list(stringg):
    words = stringg.split()
    for word in words:
        if len(word) < 5:
            print("Is less then 5")
        else:
            print("Is more then 5")

    
print(change_list("I am 23 years old"))