'''4. Student Grading System'''

name=input("Enter your name : ")
marks=input("Enter marks for 5 subjects (comma-separated) : ").split(",")
total_marks=500
scored_marks=0
for mark in marks:
    scored_marks+=int(mark)
print(f"Marked acquired = {scored_marks}")
percentage=(scored_marks/total_marks)*100
print(f"Percentage = {percentage}")
if percentage>=85:
    print("Grade = 'A'")
elif percentage>65 and percentage<85:
    print("Grade = 'B'")
elif percentage>45 and percentage<65:
    print("Grade = 'C'")
else:
    print("Grade = 'Fail'")
