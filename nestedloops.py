#print Username and password
username=input('enter the name:')
password=input('enter the value:')
if username=="Architha":
    print("welcome")
    if password=="1234":
        print("login")
    else:
        print("invaild")
else:
    print("invaild details")


#print Ticket prices according to the age    
age = int(input("Enter the age: "))

if age <= 5:
    print("Ticket price is free")
elif age <= 17:
    print("Ticket price is 100")
elif age <= 60:
    print("Ticket price is 250")
else:
    print("Ticket price is 120")


#print weekend or weekdays
day=input("enter day:")
weekday=["mon","tue","wed","thur","fri"]
weekend=["sat","sun"]
if day in weekday:
    print("week day")
elif day in weekend:
    print("weekend")
else:
    print("invaild day")
