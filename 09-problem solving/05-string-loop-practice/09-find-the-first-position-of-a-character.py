# You are given a string S and a character C. Find the index of the first occurrence of C in S. String indexing starts from 0. If the character is not present, print -1.
s = input("Enter a string: ")
n = input("Enter required value: ")

if n in s:
    print(s.index(n))
else:
    print("-1")