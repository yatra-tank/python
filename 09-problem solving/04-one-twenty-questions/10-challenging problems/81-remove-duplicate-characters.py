# Build a string containing each character only once.
s = input("Enter a string: ")
empty_s = ""

for i in s:
    if i not in empty_s:
        empty_s += i

print(empty_s)