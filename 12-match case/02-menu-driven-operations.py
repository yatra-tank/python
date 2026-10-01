n = int(input("Enter first number: "))

choice = " "

count = 0
factor = 1

while choice != "exit":
    print("""---OPERATIONS---
1. EVEN
2. ODD
3. PRIME
4. COMPOSITE
5. EXIT""")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            if n%2 == 0:
                print("even")
            else:
                print("not an even")
        case "2":
            if n%2 != 0:
                print("odd")
            else:
                print("not an odd")
        case "3":
                while factor <= n:
                    if n%factor == 0:
                        count += 1
                    factor += 1
                if count == 2:
                    print("prime")
                else:
                    print("not a prime")