n = int(input("Enter a number: "))

if n % 5 == 0 and n % 11 == 0:
    print("Divisible by both 5 and 11")
elif n % 5 == 0:
    print("Divisible only by 5")
elif n % 11 == 0:
    print("Divisible only by 11")
else:
    print("Divisible by neither")