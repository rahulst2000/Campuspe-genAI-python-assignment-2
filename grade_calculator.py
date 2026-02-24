# The user inputs marks.
# The program checks the marks using conditions and assigns a grade.
# The final grade is displayed.

marks = float(input("Enter marks: "))
if marks >= 90:
    grade = "A+"
elif marks >= 85:
    grade = "A"
elif (marks >=80) or (marks >= 75):
    grade = "B"
elif marks >=65:
    grade = "C"
elif marks >= 35 or marks <=45:
    grade = "P"
else:
    grade = "F"
print("Grade:", grade)