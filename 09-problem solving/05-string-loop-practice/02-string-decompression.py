# For every letter, the integer immediately following it tells you how many times that letter must appear in the output.
s = input("Enter a string: ")
empty_s = ""

i = 0

while i < len(s):
    if s[i].isalpha():
        letter = s[i]

        if i + 1 < len(s) and s[i + 1].isdigit():
            number = int(s[i + 1])
            i += 1
        else:
            number = 1

        empty_s += letter * number

    i += 1

print(empty_s)