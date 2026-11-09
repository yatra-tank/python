# You are given two lowercase strings, S1 and S2. Two strings are anagrams if they contain exactly the same characters with the same frequencies, but the characters may appear in a different order.
s1 = input("Enter a string: ").strip().lower()
s2 = input("Enter another string: ").strip().lower()

count = 0

if len(s1) == len(s2):
    for i in s1:
        for j in range(len(s2)):
            if s2[j] == i:
                count += 1
                
                s2 = s2[:j] + " " + s2[j+1:]
                break 

if count == len(s1) and len(s1) > 0:
    print("anagram")
else:
    print("not an anagram")