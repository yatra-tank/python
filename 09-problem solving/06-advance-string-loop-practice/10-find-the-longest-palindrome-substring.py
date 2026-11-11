# You are given a string S. Find the length of the longest substring that is a palindrome. A substring must contain consecutive characters from the original string. For example, in babad, the longest palindromic substrings are bab and aba. Their length is 3.Print only the length of the longest palindromic substring.
s = input("Enter a string: ")
max_len = 0

for i in range(len(s)):
    sub = ""
    rev = ""
    for j in range(i, len(s)):
        sub = sub + s[j]
        rev = s[j] + rev
        
        if sub == rev:
            if len(sub) > max_len:
                max_len = len(sub)

print(max_len)