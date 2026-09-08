n = int(input("Enter a number: "))

if n < 0:
    print("Negative")
elif n <= 10:
    print("Number is between 0 and 10")
elif n <= 50:
    print("Number is between 11 and 50")
elif n <= 100:
    print("Number is between 51 and 100")
else:
    print("Above 100")