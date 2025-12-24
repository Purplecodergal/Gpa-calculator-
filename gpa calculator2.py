# Function to convert score to grade point
def score_to_point(score):
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


# List to hold all students
students = [
    {
        "id": "SEN001",
        "name": "Abdulhammid Ibrahim",
        "level": "200 Level",
        "courses": {
            "CSC201": 78,
            "CSC203": 65,
            "MAT201": 72,
            "SEN201": 60,
            "GST201": 55
        }
    },
    {
        "id": "SEN002",
        "name": "Salihi Salisu Adam",
        "level": "200 Level",
        "courses": {
            "CSC201": 68,
            "CSC203": 70,
            "MAT201": 58,
            "SEN201": 62,
            "GST201": 80
        }
    },
    {
        "id": "SEN003",
        "name": "Ahmadu Yusuf Pallomi",
        "level": "200 Level",
        "courses": {
            "CSC201": 45,
            "CSC203": 50,
            "MAT201": 65,
            "SEN201": 72,
            "GST201": 60
        }
    },
    {
        "id": "SEN004",
        "name": "Mahmud Bello Ibrahim ",
        "level": "200 Level",
        "courses": {
            "CSC201": 40,
            "CSC203": 55,
            "MAT201": 60,
            "SEN201": 48,
            "GST201": 52
        }
    },
    {
        "id": "SEN005",
        "name": "zainab Sadiq Wada",
        "level": "200 Level",
        "courses": {
            "CSC201": 85,
            "CSC203": 78,
            "MAT201": 90,
            "SEN201": 88,
            "GST201": 70
        }
    }
]


# Calculate and display GPA for each student
for student in students:
    total_points = 0
    total_courses = len(student["courses"])

    for score in student["courses"].values():
        total_points += score_to_point(score)

    gpa = total_points / total_courses

    print("================================")
    print("Student ID:", student["id"])
    print("Name:", student["name"])
    print("Level:", student["level"])
    print("GPA:", round(gpa, 2))