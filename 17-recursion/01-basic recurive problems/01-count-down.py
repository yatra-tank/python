# Write countdown(n) that prints every integer from n down to 1, then prints "Done!". Constraint: n is a non-integer integer.
def countdown(n):
    if n == 0:
        print("Done!")
        return
    print(n)
    countdown(n - 1)
(countdown(3))
(countdown(0))