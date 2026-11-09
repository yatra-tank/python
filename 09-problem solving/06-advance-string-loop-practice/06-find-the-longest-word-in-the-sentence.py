# You are given a sentence containing lowercase English words separated by single spaces. Find and print the longest word. If two or more words have the same maximum length, print the word that appears first. Do not use split() or a list.
s = input("Enter a string: ")

current = ""
longest = ""

for i in s + " ":
    if i != " ":
        current += i
    else:
        if len(current) > len(longest):
            longest = current
        current = ""

print(longest)