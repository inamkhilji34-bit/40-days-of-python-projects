grades = {
    "Ali": [90,34,56,90,34],
    "Ahmad":[90,43,34,54],
    "Zain":[90,44,89,34],
    "Ikram":[34,50,56]
}
while True:
    try:
        menu = int(input("1.Add Student \n2.View grades \n3.Remove a student \n4.Quit\n"))
    except ValueError:
        print("Enter a valid number (1-4)")
        continue
    match menu:
        case 1:
            std_name = input("Enter student name: ")
            grd = []
            while True:
                try:
                    subjects = int(input("How many subjects do you have: "))
                    break
                except ValueError:
                    print("Enter a valid number.")
                
            while len(grd)<subjects:
                try:
                    n = int(input(f"Enter Subject {len(grd)+1} marks: "))
                    if 0 <= n <= 100:
                        grd.append(n)
                    else:
                        print("Enter valid grades (0-100)")
                except ValueError:
                    print("Enter a valid number.")
                continue
            grades[std_name] = grd
            print(f"{std_name} added.")
                
        case 2:
            if not grades:
                print("No student found.")
            else:
                print(f"\n{'Rank':>5} {'Students':<13} {'Subjects':>10} {'Total Marks':>12} {'Average':>10}")
                print("-" * 55)

                # ── Pass 1: calculate all averages first ──
                student_averages = {}
                for student, score in grades.items():
                    student_averages[student] = sum(score) / len(score)

                # ── Sort by average to get ranks ──
                ranked = sorted(student_averages.items(), key=lambda x: x[1], reverse=True)

                # ── Pass 2: print with correct rank ──
                all_average = []
                for rank, (student, average) in enumerate(ranked, start=1):
                    score       = grades[student]
                    subjects    = len(score)
                    total_marks = sum(score)
                    all_average.append(average)
                    print(f"{rank:>5} {student:<13} {subjects:>10} {total_marks:>12} {average:>10.2f}")

                print("-" * 55)
                class_average = sum(all_average) / len(all_average)
                print(f"{'Class Average':<30} {class_average:>10.2f}")

        case 3:
            std_name = input("Enter student name: ")
            if std_name in grades:
                grades.pop(std_name)
                print(f"{std_name} removed.")
            else:
                print("Student not found.")
        case 4:
            print("Good Bye.")
            exit()
