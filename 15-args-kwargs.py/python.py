def divide(c, *args, d = 20, **kwargs):
    return args, kwargs, c + d
print(divide(14, 15, 2, 32, 52, p = 67))