# 2)კომენტარის სახით ახსენით რამდენი ცვლადია მოცემულ ფოტოში შექმნილი,დაწერეთ თქვენი პასუხი და ახსენით ასევე რატომ,ასევე შექმენით სამი ცვლადი იგივენაირად და ახსენით რასაც გააკეთებთ კომენტარის სახით
 
name = "goga"
name = "giorgi"
namE = "lasha"
NAME = "zoia"


# კოდის წერის დროს თავიდან ჩვენ შევქმენით ცვლადი სახელად name მნიშვნელობით "goga", მაგრამ იმის შემდეგ რაც შემდეგ ხაზზე ჩვენ ზუსტად იგივე სახელით name, შევქმენით ახალი ცვლადი მნიშვნელობით "giorgi", ახლა წინა ცვლადი name განახლდა და მიეცა ახალი მნიშვნელობა "giorgi", ხოლო ცვლადი name მნიშვნელობით "goga"-ს გამოყენება შეგვეძლება მხოლოდ იმ შემთხვევსი, თუ ამ ცვლადს მაშინვე გამოვიძახებთ ახალი name ცვლადის შექმნამდე:

name = "goga"
print(name)
name = "giorgi"


# namE და NAME ასევე კიდევ ორი ერთმანეთსგან განსხვავებული ცვლადებია, რადგან პიტონი არის ქეის-სენსიტუირი პროგრამა, რაც ნიშნავს რომ NAME არ არის იგივე რაც name ან namE. ჩვენ თავიდან შევქმენით ცვლადი მაგრამ შემდეგ განვაახლეთ, და შემდეგ შევქმენით დამატებით კიდევ 2 ცვლადი, ამიტომ თუ ჩვენ გავაგრძელებთ ახალ ხაზზე კოდის დაწერას, მაშინ ამ მომენტში გვაქვს 3 ცვლადი რომლის გამოყენებაც შეგვიძლია.
