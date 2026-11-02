# Find perfect numbers up to N using divisor sums.
n = int(input("Enter a number: "))

sum = 0
i = 1

while i <= n:
  if n % i == 0:
    # print(i)
    sum += i
  i += 1

print(sum)