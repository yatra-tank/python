# Generate all pairs from 1..N and find greatest product.
n = int(input("Enter a number: "))
greatest = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        product = i * j

        if product > greatest:
            greatest = product

print("Pair:", i, j)
print("Greatest product:", greatest)