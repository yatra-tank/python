# You are given two strings, S1 and S2. Check whether S2 can be obtained by rotating S1. A rotation moves characters from one end of the string to the other without changing their relative order.
s1 = input("Enter a string: ")
s2 = input("Enter another string: ")

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("yes")
else:
    print("no")