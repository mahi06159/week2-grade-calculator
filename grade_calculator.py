# Student Grade Calculator
# Week 2 Project - Control Flow & Data Structures
# Name: Your Name

# ---------- COLOR CODES ----------
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RED = "\033[91m"
RESET = "\033[0m"

# ---------- GRADE FUNCTION ----------
def calculate_grade(avg):
    if avg >= 90:
        return "A", "Excellent! Keep up the great work!", GREEN
    elif avg >= 80:
        return "B", "Very Good! You're doing well.", BLUE
    elif avg >= 70:
        return "C", "Good. Room for improvement.", YELLOW
    elif avg >= 60:
        return "D", "Needs Improvement. Please study more.", YELLOW
    else:
        return "F", "Failed. Please seek help from teacher.", RED

# ---------- INPUT VALIDATION ----------
def get_valid_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if 0 <= value <= 100:
                return value
            else:
                print("Enter value between 0 and 100")
        except ValueError:
            print("Invalid input! Enter a number.")

# ---------- SEARCH ----------
def search_student(results, name):
    for student in results:
        if student["name"].lower() == name.lower():
            return student
    return None

# ---------- SAVE TO FILE ----------
def save_results(results):
    with open("results_sample.txt", "w") as f:
        for s in results:
            f.write(f"{s['name']} | Avg: {s['avg']:.1f} | Grade: {s['grade']}\n")
    print("Results saved to results_sample.txt")

# ---------- MAIN PROGRAM ----------
def main():
    print("=" * 50)
    print("      STUDENT GRADE CALCULATOR")
    print("=" * 50)

    # Number of students
    while True:
        try:
            n = int(input("Enter number of students: "))
            if n > 0:
                break
            print("Enter a positive number")
        except ValueError:
            print("Invalid number")

    results = []

    # Collect Data
    for i in range(n):
        print(f"\n=== STUDENT {i+1} ===")
        name = input("Student name: ").strip()
        while name == "":
            name = input("Name cannot be empty. Enter again: ")

        math = get_valid_number("Math: ")
        science = get_valid_number("Science: ")
        english = get_valid_number("English: ")

        avg = (math + science + english) / 3
        grade, comment, color = calculate_grade(avg)

        results.append({
            "name": name,
            "avg": avg,
            "grade": grade,
            "comment": comment,
            "color": color
        })

    # Display Table
    print("\n" + "=" * 60)
    print("RESULTS SUMMARY")
    print("=" * 60)
    print(f"{'Name':<20} {'Avg':<6} {'Grade':<6} Comment")
    print("-" * 60)

    for s in results:
        print(f"{s['name']:<20} {s['avg']:<6.1f} {s['color']}{s['grade']}{RESET}     {s['comment']}")

    # Statistics
    avgs = [s["avg"] for s in results]
    print("\nCLASS STATISTICS")
    print("=" * 60)
    print(f"Total Students: {len(results)}")
    print(f"Class Average: {sum(avgs)/len(avgs):.1f}")
    print(f"Highest Average: {max(avgs):.1f}")
    print(f"Lowest Average: {min(avgs):.1f}")

    # Menu
    while True:
        print("\nMENU")
        print("1. Search Student")
        print("2. Save Results to File")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            name = input("Enter student name: ")
            student = search_student(results, name)
            if student:
                print(f"{student['name']} | Avg: {student['avg']:.1f} | Grade: {student['grade']}")
            else:
                print("Student not found")

        elif choice == "2":
            save_results(results)

        elif choice == "3":
            print("Thank you for using the Grade Calculator!")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
