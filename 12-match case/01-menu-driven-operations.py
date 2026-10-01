# while True:
#     print("""---OPERATIONS---
# 1. ADDITION
# 2. SUBTRACTION
# 3. MULTIPLICATION
# 4. DIVISION
# 5. FLOOR DIVISION
# 6. EXIT""")

#     choice = input("Enter your choice: ")

#     if choice == "6":
#         print("Exited")
#         break

#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))

#     match choice:
#         case "1":
#             print("Addition =", num1 + num2)

#         case "2":
#             print("Subtraction =", num1 - num2)

#         case "3":
#             print("Multiplication =", num1 * num2)

#         case "4":
#             print("Division =", num1 / num2)

#         case "5":
#             print("Floor Division =", num1 // num2)

#         case _:
#             print("Invalid choice")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

choice = ""

while choice != "exit":
    print("""---OPERATIONS---
1. ADDITION
2. SUBTRACTION
3. MULTIPLICATION
4. DIVISION
5. FLOOR DIVISION
6. EXIT""")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            print(a + b)

        case "2":
            print(a - b)

        case "3":
            print(a * b)

        case "4":
            print(a / b)

        case "5":
            print(a // b)

        case "6":
            choice = "exit"

        case "exit":
            print("Exited")

        case _:
            print("Invalid choice")