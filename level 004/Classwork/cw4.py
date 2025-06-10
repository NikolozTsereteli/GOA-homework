# 4) მომხმარებელს შემოატანინეთ რიცხვი და ამ რიცხვამდე დაპრინტეთ ყველა ეს რიცხვი


Number = int(input("Enter a number here: "))
counter = 1
while counter < Number:
    print(counter)
    counter += 1
print("Iteration of numbers from 1 to " + str(Number) + " completed.")
