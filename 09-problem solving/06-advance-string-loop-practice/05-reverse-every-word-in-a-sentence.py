# You are given a sentence containing lowercase English words separated by single spaces. Reverse each word individually, but keep the order of the words unchanged.
s = input("Enter a string: ").split()
empty_s = ""

for i in s:
    empty_s += " " + i[::-1]

print(empty_s.lstrip())