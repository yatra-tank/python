n1, n2 = map(int, input("Enter two numbers separate by commas: ").split(",")[:2])
print("""---OPERATIONS---
    1.ADDITION
    2.SUBTRACTION
    3. DIVISION
    4. MULTIPLICATION
    5. FLOOR DIVISION""")
operation = int(input("ENter your operation number: "))
if operation == 1:
    print(n1 + n2)
elif operation == 2:
    print(n1 - n2)
elif operation == 3:
    print(n1 / n2)
elif operation == 4:
    print(n1 * n2)
elif operation == 5:
    print(n1 // n2)
else:
    print("invalid operation")