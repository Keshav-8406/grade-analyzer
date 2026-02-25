 # Task 1
def process_scores(students):
    averages = {}
    for name, scores in students.items():
        avg = round(sum(scores) / len(scores), 2)
        averages[name] = avg
    return averages

# Task 2
def classify_grades(averages):
    classified = {}
    A = 90
    B = 75
    C = 60

    for name, avg in averages.items():
        if avg >= A:
            grade = "A"
        elif avg >= B:
            grade = "B"
        elif avg >= C:
            grade = "C"
        else:
            grade = "F"

        classified[name] = (avg, grade)
    return classified


# Task 3
def generate_report(classified, passing_avg=70):  
    print("===== Student Grade Report =====\n")

    passed = 0
    total = len(classified)

    for name, (avg, grade) in classified.items():
        status = "PASS" if avg >= passing_avg else "FAIL"

        if status == "PASS":
            passed += 1

        print(name)
        print(f"| Avg: {avg:.2f}")
        print(f"Grade: {grade}")
        print(f"Status: {status}\n")

    failed = total - passed

    print("Total Students:", total)
    print("Passed:", passed)
    print("Failed:", failed)
    return passed

# Main Grade Distributing Programme
if __name__ == "__main__":
    students = {
        "Alice": [85, 88, 90, 82],
        "Bob": [60, 65, 63, 62],
        "Clara": [95, 98, 92, 100]
    }

    averages = process_scores(students)
    classified = classify_grades(averages)
    generate_report(classified)
