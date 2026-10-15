# Print ordered pairs whose positions are different.
s = input("Enter a string: ")

for i in s:
    for j in s:
        if i != j:
            print(f"{i} {j},", end= " ")