# 4)1 დან 100 მდე გამოიტანეთ მხოლოდ კენტი რიცხვები,შეასრულეთ while loop / for loop ორივეთი 


for i in range(1, 100):
    if i % 2 != 0:
        print(i)


i = 1
while i < 100:
    if i % 2 != 0:
        print(i)
    i += 1