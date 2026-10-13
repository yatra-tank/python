# Take a positive integer n greater than 1. Search for a divisor from 2 through n - 1. If a divisor is found, print "Not prime" and stop. If the loop finishes without finding one, print "Prime" using for-else.
n = int(input("Enter a number: "))

for i in range(2, n):
    if n % i == 0:
        print("Not prime")
        break
else:
    print("Prime")