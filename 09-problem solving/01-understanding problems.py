# 1
a = int(input())
b = int(input())

if a > b:
    print(a)
else:
    print(b)


# 2
marks = int(input())

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")


# 3
length = float(input())
width = float(input())

area = length * width
perimeter = 2 * (length + width)

print(area)
print(perimeter)


# 4
number = int(input())

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# 5
price = float(input())

if price >= 1000:
    discount = price * 0.10
    final_price = price - discount
else:
    final_price = price

print(final_price)