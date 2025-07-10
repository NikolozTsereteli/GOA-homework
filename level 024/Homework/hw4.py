# 4)შექმენი ფუნქცია რომელსაც გადაეცემა რაიმე რიცხვი,შენი დავალებაა 0 დან ამ რიცხვამდე დაითვალო 3 ის გამოტოვებით FOR LOOP/WHILE LOOP


def for_while(num):
    for i in range(0, num + 1):
        if i % 3 != 0:
            print(i)

    j = 0
    while j < num + 1:
        if i % 3 != 0:
            print(j)
        j += 1

print(for_while(100))