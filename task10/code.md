### 1. Problem Statement

Develop a Python program to analyze student performance across multiple examinations. Calculate subject-wise average scores, compare assessment marks to identify improvements and declines, detect consistently weak subjects, and classify students based on their overall performance using specified criteria. Generate a final performance report for each student.

### 2. Algorithm

1. Start the program.
2. Enter the number of students.
3. Enter the student name and number of subjects.
4. Enter subject names.
5. Enter marks obtained in multiple examinations.
6. Calculate the average marks for each subject.
7. Compare marks across examinations.
8. Identify improvements and declines in marks.
9. Detect consistently weak subjects.
10. Calculate the overall average score.
11. Classify students based on performance criteria.
12. Display the student performance report.
13. Repeat for all students.
14. Stop the program.

### 3. Flowchart (Mermaid)
```mermaid
flowchart TD
    A([Start]) --> B[Enter Number of Students]
    B --> C[Enter Student Details]
    C --> D[Enter Subject Names]
    D --> E[Enter Examination Marks]
    E --> F[Calculate Subject Averages]
    F --> G[Compare Examination Scores]
    G --> H[Identify Improvements and Declines]
    H --> I[Identify Weak Subjects]
    I --> J[Calculate Overall Average]
    J --> K{Check Performance}
    K -->|90 and Above| L[Excellent]
    K -->|75 to 89| M[Very Good]
    K -->|50 to 74| N[Average]
    K -->|Below 50| O[Needs Improvement]
    L --> P[Display Performance Report]
    M --> P
    N --> P
    O --> P
    P --> Q{More Students?}
    Q -->|Yes| C
    Q -->|No| R([Stop])
```
### 5. Sample Input

```
Enter number of students: 1

Student 1
Enter student name: Ravi
Enter number of subjects: 2

Enter subject name: Python
Enter Exam 1 marks: 60
Enter Exam 2 marks: 75
Enter Exam 3 marks: 85

Enter subject name: Maths
Enter Exam 1 marks: 30
Enter Exam 2 marks: 35
Enter Exam 3 marks: 38
```

### 6. Sample Output

```
Student 1

Subject Average: 73.33
Performance: Improved

Subject Average: 34.33
Performance: Improved
Weak Subject: Maths

--- Student Performance Report ---
Student Name: Ravi
Overall Average: 53.83
Weak Subjects: 1
Classification: Average

Performance Analysis Completed
```

