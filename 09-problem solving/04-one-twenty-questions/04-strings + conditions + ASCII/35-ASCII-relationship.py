# Classify each pair as Increasing, Decreasing or Same by ASCII value.
s = input("Enter a string: ")

for i in s:
    for j in s:
        if i < j:
            print(f"{i} {j} -> Increasing,", end= " ")
        elif i > j:
            print(f"{i} {j} -> Decreasing,", end= " ")
        else:
            print(f"{i} { j} -> Same,")