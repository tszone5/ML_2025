print("Student Grading System")
print("----------------------")

marks = float(input("Enter student marks (0-100): "))

if marks > 100 or marks < 0:
    print("Invalid marks! Please enter between 0-100")
elif marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: Fail")
