# 7)შექმენით ორი სია,პირველ სიაში გექნებთ მხოლოდ string ტიპის მონაცემები მეორე სიაშ კი მხოლოდ ინტეჯერები,თქვენი დავალებაა ეს ორი სია გააერთანოთ extend ფუნქციის დახმარებით,შემდეგ შექმენით კიდევ ერთი სია სადაც გექნებათ მხოლოდ float ტიპის მონაცემები და გააერთიანეთ პირვეი ორი გაერთიანებული სია მესამე სიაში


Groups = ["Critics", "Apologists", "Atheists", "Skeptics", "Scholars", "Believers"]
Numbers = [67, 343, 85, 26, 14, 68, 34, 79, 89, 53, 69, 897, 347]
Groups.extend(Numbers)
Floats = [5.6, 3.67, 789.1, 4785.5745, 67.45, 6.6, 9.9, 7.89, 9.34, 7.01]
Groups.extend(Floats)
print(Groups)
