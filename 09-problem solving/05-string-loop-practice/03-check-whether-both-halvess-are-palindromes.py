# You are given a string str and its length N. The value of N is always even.
def palindrome(s):
    length = len(s)
    mid = length // 2

    first = s[:mid]
    second = s[mid:]

    if check(first) and check(second):
        return "yes"
    else:
        return "no"

def check(s):
    if s == s[::-1]:
        return True
    else:
        return False

s = input("Enter a string: ")
print(palindrome(s))