name1 = input("Enter name of person 1: ")
age1 = int(input("Enter age of person 1: "))

name2 = input("Enter name of person 2: ")
age2 = int(input("Enter age of person 2: "))

name3 = input("Enter name of person 3: ")
age3 = int(input("Enter age of person 3: "))

if age1 < age2 and age1 < age3:
    print(name1, "is the youngest")
elif age2 < age1 and age2 < age3:
    print(name2, "is the youngest")
elif age3 < age1 and age3 < age2:
    print(name3, "is the youngest")
elif age1 == age2 and age2 == age3:
    print("All three have the same age")
elif age1 == age2 and age1 < age3:
    print(name1, "and", name2, "are the youngest")
elif age1 == age3 and age1 < age2:
    print(name1, "and", name3, "are the youngest")
else:
    print(name2, "and", name3, "are the youngest")