# 5)1 დან 50 მდე გამოიტანეთ მხოლოდ ის რიცხვები რომლებიც იყოფიან 5 ზეც და 3 ზეც,შეასრულეთ while loop / for loop ორივეთი


for i in range(1, 50):
    if i % 5 == 0 and i % 3 == 0:
        print(i)


i = 1
while i < 50:
    if i % 5 == 0 and i % 3 == 0:
        print(i)
    i += 1