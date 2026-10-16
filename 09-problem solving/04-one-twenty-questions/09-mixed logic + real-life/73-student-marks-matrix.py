# Input marks for 3 students and 4 subjects; print marks, total and average.
for i in range(1, 4):
    total = 0
    for j in range(4):
        print("Enter data from student", i)
        n = int(input("Enter your marks: "))
        total += n
        avg = total/4
    print("Student", i, "total: ", total, "average: ", avg, end= " ")
    print()