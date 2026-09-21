age = int(input("Enter student age: "))
marks = float(input("Enter marks: "))
income = float(input("Enter family income: "))
attendance = float(input("Enter attendance percentage: "))

if age >= 18 and age <= 25 and marks >= 85 and attendance >= 75 and income <= 300000:
    print("Scholarship Approved")
else:
    print("Scholarship Rejected")

    if age < 18 or age > 25:
        print("Reason: Age not between 18 and 25")

    if marks < 85:
        print("Reason: Marks below 85")

    if attendance < 75:
        print("Reason: Attendance below 75")

    if income > 300000:
        print("Reason: Family income above ₹300000")