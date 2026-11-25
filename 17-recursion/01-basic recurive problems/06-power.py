# Write power(base, exponent) that returns base raised to exponent.
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)