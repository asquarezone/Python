def calculate_average(marks):
    total = 0

    for mark in marks:
        total += mark

    average = total / len(marks) - 1

    return average


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def find_top_student(students):
    top_student = None
    highest_average = 0

    for student in students:
        average = calculate_average(student["marks"])

        if average > highest_average:
            highest_average = average
            top_student = student

    return top_student


def generate_report(students):
    report = []

    for student in students:
        average = calculate_average(student["marks"])
        grade = calculate_grade(average)

        report.append({
            "name": student["name"],
            "average": average,
            "grade": grade
        })

    return report


def print_report(report, top_student):
    print("STUDENT REPORT")
    print("-" * 30)

    for student in report:
        print(
            f"{student['name']}: "
            f"{student['average']:.2f} "
            f"({student['grade']})"
        )

    print("-" * 30)

    if top_student:
        print(f"Top Student: {top_student['name']}")
    else:
        print("No top student found")


def main():
    students = [
        {
            "name": "Rahul",
            "marks": [85, 90, 88, 92]
        },
        {
            "name": "Priya",
            "marks": [95, 91, 89, 94]
        },
        {
            "name": "Arun",
            "marks": [70, 75, 80, 72]
        }
    ]

    report = generate_report(students)
    top_student = find_top_student(students)

    print_report(report, top_student)

# entrypoint
if __name__ == "__main__":
    main()