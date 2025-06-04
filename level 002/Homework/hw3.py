# 3) True or True and False or True and False რას გამოგვიტანს შედეგად


# True or True and False or True and False. რადგან ჩვენ ვიცით რომ Python-ი უფრო მაღალ პრიორიტეტს ანიჭებს and ლოგიკურ ოპერატორს ვიდრე or ლოგიკურ ოპერატორს, ჩვენ ვიცით რომ კოდი ჯერ გამოითვლის and ლოგიკურ ოპერატორებს - True or (True and False) or (True and False) - True or False or False - (True or False) or False - True or False - True.

print(True or True and False or True and False)