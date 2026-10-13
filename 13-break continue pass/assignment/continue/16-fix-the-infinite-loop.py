# The following program does not finish. Rewrite it so that it skips 3 and prints 1, 2, 4, and 5.
n = 0

while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)