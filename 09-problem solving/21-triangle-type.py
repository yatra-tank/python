a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle")
elif a == b and b == c:
    print("Equilateral")
elif a == b or a == c or b == c:
    print("Isosceles")
else:
    print("Scalene")