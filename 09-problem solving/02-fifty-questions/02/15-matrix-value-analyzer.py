even = 0
odd = 0
positive = 0
negative = 0
zero = 0
highest = None

for i in range(3):
    for j in range(3):
        n = int(input("Enter number: "))

        if n % 2 == 0:
            even += 1
        else:
            odd += 1

        if n > 0:
            positive += 1
        elif n < 0:
            negative += 1
        else:
            zero += 1

        if highest is None or n > highest:
            highest = n

print("Even:", even)
print("Odd:", odd)
print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)
print("Largest:", highest)