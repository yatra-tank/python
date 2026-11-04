# You are given a string S. Reverse the string without using slicing with a step of -1 and without using built-in reverse methods.
s = input("Enter a string: ")
empty_s = ""

for i in s:
    empty_s = i + empty_s

print(empty_s)