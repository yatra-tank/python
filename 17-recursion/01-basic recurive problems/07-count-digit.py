# Write count_digits(n) that returns the number of digits in a non-negative integer.
def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)