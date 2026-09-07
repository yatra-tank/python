first_number, second_number = map(int, input("Enter two numbers separated by commas: ").split(",")[:2])
print("""---OPERATIONS---
1. ADDITION
2. SUBTRACTION
3. DIVISION
4. MULTIPLICATION
5. FLOOR DIVISION""")
operation = int(input("ENter your operation number: "))
if operation == 1:
    print(first_number + second_number)
elif operation == 2:
    print(first_number - second_number)
elif operation == 3:
    print(first_number / second_number)
elif operation == 4:
    print(first_number * second_number)
elif operation == 5:
    print(first_number // second_number)
else:
    print("invalid operation")