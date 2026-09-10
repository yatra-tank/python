n = int(input("Enter a number: "))
sq = n ** 2
divisor = 10

while divisor <= n:
    divisor *= 10

left = sq // divisor
right = sq % divisor

if left != 0 and right != 0 and left + right == n:
    print("kaprekar number")
else:
    print("not kaprekar number")