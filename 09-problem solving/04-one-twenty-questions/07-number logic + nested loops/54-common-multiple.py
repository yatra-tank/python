# Generate multiples and print common multiples up to a limit.
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
limit = int(input("Enter a limit: "))

count = 0

for i in range(1, limit + 1):
    for j in range(1, limit + 1):
        if i * a == j * b and i * a <= limit:
            print(i * a, end=" ")
            count += 1
            break

if count == 0:
    print("No common multiples")