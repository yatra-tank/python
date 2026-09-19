total = 0
grade = "F"
flag = True

for i in range(5):
    marks = int(input("Enter your marks: "))
    total += marks
    if marks < 35:
        flag = False

if flag:
    pr = total / 5
    if pr >= 90:
        grade = "A+"
        print("Your percentage: ", pr)
    elif pr >= 80:
        grade = "A"
        print("Your percentage: ", pr)
    elif pr >= 70:
        grade = "B"
        print("Your percentage: ", pr)
    elif pr >= 60:
        grade = "C"
        print("Your percentage: ", pr)
    elif pr >= 50:
        grade = "D"
        print("Your percentage: ", pr)
    else:
        grade = "F"
        print("Your percentage: ", pr)
else:
    grade = "F"
    print("You've failed subject.")

print("Your total marks obtained: ", total)
print("Your grade: ", grade)
if flag:
    print("You're Pass")
else:
    print("You're Fail")