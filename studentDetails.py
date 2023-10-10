# Dictionary Challenge
# Creating the Dictionary with student details

Student = {}

for i in range(3):
    name = input("Enter your name:")
    rool_no = input("Enter  your USN: ")
    dept = input("Enter your department: ")

    Student[name] = {"USN: ": rool_no, "Name: ": name, "Department: ": dept}

print(Student)
