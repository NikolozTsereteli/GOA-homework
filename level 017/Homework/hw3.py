# 3. შექმენით ფუნქცია, რომელიც მომხმარებლის შემოტანილ float ტიპის მონაცემს დაშლის. მაგალითად 30.7 რომ ავიღოთ, შედეგი ასეთი უნდა იყოს: '30 + 0.7 = 30.7' .


num = float(input("Enter a random float point number here: "))
def divide(num):
    num1 = num - int(num)
    return str(int(num)) + " + " + str(num1) + " = " + str(num)

print(divide(num))
