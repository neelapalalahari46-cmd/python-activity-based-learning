# Student Performance Trend Analysis

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")
    subjects = int(input("Enter number of subjects: "))

    total = 0
    weak_subjects = 0

    for j in range(subjects):
        subject = input("\nEnter subject name: ")

        m1 = float(input("Enter Exam 1 marks: "))
        m2 = float(input("Enter Exam 2 marks: "))
        m3 = float(input("Enter Exam 3 marks: "))

        average = (m1 + m2 + m3) / 3
        total += average

        print("Subject Average:", round(average, 2))

        # Compare examination marks
        if m3 > m1:
            print("Performance: Improved")
        elif m3 < m1:
            print("Performance: Declined")
        else:
            print("Performance: No Change")

        # Check weak subjects
        if m1 < 40 and m2 < 40 and m3 < 40:
            print("Weak Subject:", subject)
            weak_subjects += 1

    # Overall performance
    overall = total / subjects

    print("\n--- Student Performance Report ---")
    print("Student Name:", name)
    print("Overall Average:", round(overall, 2))
    print("Weak Subjects:", weak_subjects)

    if overall >= 90:
        print("Classification: Excellent")
    elif overall >= 75:
        print("Classification: Very Good")
    elif overall >= 50:
        print("Classification: Average")
    else:
        print("Classification: Needs Improvement")

print("\nPerformance Analysis Completed")
