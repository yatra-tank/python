day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if year <= 0 or month < 1 or month > 12 or day < 1:
    print("Invalid date")
elif month == 2:
    if year % 400 == 0:
        if day <= 29:
            print("Valid date")
        else:
            print("Invalid date")
    elif year % 100 == 0:
        if day <= 28:
            print("Valid date")
        else:
            print("Invalid date")
    elif year % 4 == 0:
        if day <= 29:
            print("Valid date")
        else:
            print("Invalid date")
    elif day <= 28:
        print("Valid date")
    else:
        print("Invalid date")
elif month == 4 or month == 6 or month == 9 or month == 11:
    if day <= 30:
        print("Valid date")
    else:
        print("Invalid date")
elif day <= 31:
    print("Valid date")
else:
    print("Invalid date")