print("=== Student Result System ===")

name = input("Enter student name: ")

m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))

total = m1 + m2 + m3
average = total / 3

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

if average >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")
