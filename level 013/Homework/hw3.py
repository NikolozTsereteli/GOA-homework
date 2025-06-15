# 3) შექმენით ფუნქცია, რომელიც მომხმარებლის შემოტანილ float ტიპის მოცანემს გახლიჩავს. შედეგი ასე რომ იყოს :  19.27 => 19 + 0.27 


float_number = float(input("Enter a float point number here: "))
def split_floats(float_number):
    decimal_number = float_number - int(float_number)
    integer = int(float_number)
    split = str(integer) + " + " + str(decimal_number)
    print(split) 

split_floats(float_number)