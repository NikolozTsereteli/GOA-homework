# 5)დაწერეთ ფუნქცია concat_strings(words), რომელიც იღებს სტრინგების სიას და აბრუნებს ერთ სტრინგად გაერთიანებულ ყველა სიტყვას.

def concat_strings(words):
    return " ".join(words)


print(concat_strings(["I", "am", "a", "human", "being", "with", "human", "nature"]))