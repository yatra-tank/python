# For every word pair print lengths and first-character comparison.
s = input("Enter a string: ")
words = s.split()

for i in range(len(words) - 1):
    a = words[i]
    b = words[i + 1]

    if a[0] == b[0]:
        print("Same", end=" ")
    else:
        print("Different", end= " ")