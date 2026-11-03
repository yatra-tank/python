# Check each word for palindrome using character comparisons, not slicing.
s = input("Enter a string: ")
words = s.split()

for i in words:
    count = 0

    for j in range(len(i) // 2):
        if i[j] == i[len(i) - 1 - j]:
            count += 1

    if count == len(i) // 2:
        print(i)