# Print tables 1..N, each from ×1 to ×10.
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()