# Write digit_sum(n) that returns the sum of the digits of a non-negative integer.
def digit_sum(n):
    if n == 0:
        return 0
    return (n % 10) + digit_sum(n // 10)