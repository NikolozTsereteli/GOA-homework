# 7)for loop ის გამოყენებით ერთიდან 20 გამოიტანეთ ყველა რიცხვის ჯამი,იგივე შეასრულეთ while loop


sum = 0
for i in range(1, 20):
    sum += i
print(sum)

i = 1
sum = 0
while i < 20:
    sum += i
    i += 1
print(sum)
