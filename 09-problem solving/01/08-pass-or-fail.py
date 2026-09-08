n = float(input("Enter your marks: "))

if n < 0 or n > 100:
    print("Invalid marks")
elif n >= 40:
    print("Pass")
else:
    print("Fail")