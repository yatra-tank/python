# Find the longest palindrome among words.
s = input("Enter a string: ")
words = s.split()
longest = ""

for i in words:
    count = 0

    for j in range(len(i) // 2):
        if i[j] == i[len(i) - 1 - j]:
            count += 1

    if count == len(i) // 2:
        if len(i) > len(longest):
            longest = i

print("Longest palindrome:", longest)