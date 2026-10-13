def calculator(a, b):
    print("""--- OPERATIONS ---
    1. ADDITION
    2. SUBTRACTION
    3. MULTIPLICATION
    4. FLOOR DIVISION """)
    n = int(input("Enter desired operation: "))
    if n == 1:
        print(a + b)
    elif n == 2:
        print(a - b)
    elif n == 3:
        print(a * b)
    elif n == 4:
        print(a // b)
    else:
        print("Invalid operation.")

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
calculator(a, b)