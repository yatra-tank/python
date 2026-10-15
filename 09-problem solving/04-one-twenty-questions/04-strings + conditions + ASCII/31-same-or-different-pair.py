# Print each character pair with Same/Different and the pair itself.
s = input("Enter a string: ")

for i in range(len(s) - 1):
    a = s[i] + s[i + 1]
    
    if s[i] == s[i + 1]:
        print(f"Equal {s[i]}/{s[i+1]} is Same")
    else:
        print(f"{a} is Different")
