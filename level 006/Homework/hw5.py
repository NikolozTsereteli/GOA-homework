# 5)კომენტარის სახით ახსენით and და or ოპერატორების მუშაობის პრინციპი და მოიყვანეთ მაგალითები


# and და or არიან ლოგიკური ოპერატორები
# and ოპერატორი აბრუნებს True-ს მხოლოდ მაშინ, როცა ორივე პირობა არის True
# თუ რომელიმე პირობა არის False, შედეგიც იქნება False

# მაგალითი: 

age = 19
name = "Nika"

if age > 18 and name == "Nika":
    print("You are an adult and your name is Nika")
# დაიბეჭდება, რადგან ორივე პირობა სწორია

# or ოპერატორი აბრუნებს True-ს, მაშინაც კი, როდესაც მხოლოდ ერთი პირობაა True
# მხოლოდ მაშინ აბრუნებს False-ს, როდესაც ორივე პირობაა False

# მაგალითი

age = 16
name = "Nika"

if age > 18 or name == "Nika":
    print("Either you are an adult, or your name is Nika(or both)")
# დაიბეჭდება, რადგან ერთი პირობა მაინც არის სწორი (name == "Nika")


# and = True მხოლოდ მაშინ, როცა ორივე პირობაა True
# or = True მაშინაც კი, როცა ერთი პირობა მაინც არის True 
