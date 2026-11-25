# Write sum_to(n) that returns the sum of all integers from 1 through n.
def sum_to(n):
    if n == 0:
        return 0
    return n + sum_to(n - 1)