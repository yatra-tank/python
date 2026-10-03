# Create a student portal menu:

# 1 → View Profile
# 2 → View Courses
# 3 → View Marks
# 4 → View Attendance
# 5 → Logout
# Take the user's choice and display an appropriate message.

print("""--- STUDENT PORTAL ---
1. VIEW PROFILE
2. VIEW COURSES
3. VIEW MARKS
4. VIEW ATTENDANCE
5. LOGOUT""")

n = int(input("Enter your order: "))

match n:
    case 1:
        print("Opening profile.")
    case 2:
        print("Opening courses.")
    case 3:
        print("Opening marks.")
    case 4:
        print("Opening attendance.")
    case 5:
        print("Logging out.")
    case _:
        print("Invalid option.")