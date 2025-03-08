print("""
  ■■■■  ■   ■   ■■■■■   ■■■■   
    ■    ■■ ■■  ■     ■  ■   ■ 
    ■    ■ ■ ■  ■■■■■■  ■    ■  
■   ■    ■   ■  ■     ■  ■   ■ 
 ■■■     ■   ■  ■     ■  ■■■■
""")

def assign_grade(score):
 
    if score < 0 or score > 100:
        print("Invalid score! Please enter a value between 0 and 100.")
    elif score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

def calculate_percentage(grades):
   
    total_subjects = len(grades)
    total_sum = sum(grades)
    percentage = total_sum // total_subjects
    return percentage

# List of my brainrot subjects
subjects = ["Cal2", "Rizz", "Introvert mode", "Depression", "Economic", "Programming", "Physics", "Women", "IQ"]

grades = []
print("Enter your grades for the following subjects (whole numbers only):")

for subject in subjects:
    while True:
        try:
            grade = int(input(f"{subject} grade: "))
            if 0 <= grade <= 100:
                grades.append(grade)
                break
            else:
                print("Please enter a valid grade between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a whole number.")

percentage = calculate_percentage(grades)

print("\nYour Grade Percentage is:", percentage, "%")