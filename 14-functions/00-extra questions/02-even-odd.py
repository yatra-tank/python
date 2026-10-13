def even(n):
    if n % 2 == 0:
        print("even")
    else:
        print("not an even")

def odd(n):
    if n % 2 != 0:
        print("odd")
    else:
        print("not an odd")

def prime(n):
    count = 0
    factor = 1

    while factor <= n:
        if n % factor == 0:
            count += 1
        factor += 1

    if count == 2:
        print("prime")
    else:
        print("not a prime")

def composite(n):
    count = 0
    factor = 1

    while factor <= n:
        if n % factor == 0:
            count += 1
        factor += 1

    if count > 2:
        print("composite")
    else:
        print("not a composite")

n = int(input("Enter first number: "))
choice = " "
while choice != "5":
    print("""---OPERATIONS---
1. EVEN
2. ODD
3. PRIME
4. COMPOSITE
5. EXIT""")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        even(n)
    elif choice == "2":
        odd(n)
    elif choice == "3":
        prime(n)
    elif choice == "4":
        composite(n)
    elif choice == "5":
        print("Exit")
    else:
        print("Invalid choice")