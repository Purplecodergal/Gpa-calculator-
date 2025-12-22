def grade_point(score):
    if score >= 70:
        return 5
    elif score >= 60:
        return 4
    elif score >= 50:
        return 3
    elif score >= 45:
        return 2
    elif score >= 40:
        return 1
    else:
        return 0


courses = ["INS 201", "IFT 201", "COS 221", "NIS 212", "PST 210"]
number_of_students = 5

for student in range(1, number_of_students + 1):
    print(f"\nEnter scores for Student {student}")
    total_points = 0

    for course in courses:
        score = int(input(f"Enter score for {course}: "))
        total_points += grade_point(score)

    gpa = total_points / len(courses)
    print(f"Student {student} GPA: {gpa:.2f}")def grade_point(score):
    if score >= 70:
        return 5
    elif score >= 60:
        return 4
    elif score >= 50:
        return 3
    elif score >= 45:
        return 2
    elif score >= 40:
        return 1
    else:
        return 0


courses = ["INS 201", "IFT 201", "COS 221", "NIS 212", "PST 210"]
number_of_students = 5

for student in range(1, number_of_students + 1):
    print(f"\nEnter scores for Student {student}")
    total_points = 0

    for course in courses:
        score = int(input(f"Enter score for {course}: "))
        total_points += grade_point(score)

    gpa = total_points / len(courses)
    print(f"Student {student} GPA: {gpa:.2f}")