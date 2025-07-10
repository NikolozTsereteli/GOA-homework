# 3)შექმენით ფუნქცია რომელსაც გადაეცემა ერთი მთლიანი წინადადება,თქვენი დავალებაა ამ წინადადებაში მყოფი სიტყვები ჩაამატოთ სიაში(გამოიყენეთ შესაბამისი ფუნქცია)და შემდეგ ეს სია დაუბრუნოთ ისევ ერთ მთლიან სტრინგად(წინადადებად) მაგრამ სტრინგად დაბრუნების დროს ეს სიტყვები გამოყავით ერთმანეთისაგან @ ამ ნიშნით და ასევე ყველა სიტყვის პირველი ასო იყოს დიდი(CAPIRALIZE)


def string_to_list(sentence):
    words = sentence.split()
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    New_string = "@".join(words)
    
    return New_string

print(string_to_list("I am 19 years old"))