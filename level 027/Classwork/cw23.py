# 24)შექმენი ფუნქცია რომელსაც გადაეცემა ორი სია,შენიდვავლებაა გააერთანო ეს ორი სია ერთმანთიში(გამოიყენე შეაბამისი ფუნქცია)


def combined_lists(list1, list2):
    list1.extend(list2)
    
    return list1

print(combined_lists([1, 2, 3], [4, 5, 6])) 
