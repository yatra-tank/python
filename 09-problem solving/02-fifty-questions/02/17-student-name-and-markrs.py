# Take the name and marks of 5 students.
max_marks = -1
topper = ""

for i in range(5):
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))

    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    else:
        grade = "F"

    v = 0
    c = 0
    count = 0

    for ch in name:
        count += 1
        if ch in "aeiouAEIOU":
            v += 1
        elif ("a" <= ch <= "z") or ("A" <= ch <= "Z"):
            c += 1

    print("Grade:", grade)
    print("Vowels:", v)
    print("Characters:", count)

    if v > c:
        print("More vowels")
    elif c > v:
        print("More consonants")
    else:
        print("Equal vowels and consonants")

    if marks > max_marks:
        max_marks = marks
        topper = name

print("Topper:", topper)
print("Highest Marks:", max_marks)