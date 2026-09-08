n = int(input("Enter a number: "))

if n % 3 == 0 and n % 7 == 0:
    print("Divisible by both 3 and 7")
elif n % 3 == 0:
    print("Divisible only by 3")
elif n % 7 == 0:
    print("Divisible only by 7")
else:
    print("Divisible by neither")