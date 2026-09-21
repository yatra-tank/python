hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

if hours >= 0 and hours <= 23 and minutes >= 0 and minutes <= 59 and seconds >= 0 and seconds <= 59:
    print("Valid time")
else:
    print("Invalid time")