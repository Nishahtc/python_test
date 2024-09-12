import numpy as np

# Step 1: Data Input
def input_student_data():
    num_students = int(input("Enter the number of students: "))
    names = []
    grades = []

    for _ in range(num_students):
        name = input("Enter the student's name: ")
        names.append(name)
        # Assuming 3 subjects: Math, Science, English
        grades_input = input("Enter grades for Math, Science, English separated by spaces: ")
        grades.append(list(map(float, grades_input.split())))

    return np.array(names), np.array(grades)

# Step 2: Store Data
names, grades = input_student_data()

# Step 3: Calculate Statistics
average_grades = np.mean(grades, axis=1)
highest_grade = np.max(grades)
lowest_grade = np.min(grades)
average_subject_grades = np.mean(grades, axis=0)

# Step 4: Identify Top Performers
top_student_index = np.argmax(average_grades)
top_student_name = names[top_student_index]
top_student_average = average_grades[top_student_index]

# Step 5: Print Results
print("\nStudent Averages:")
for name, avg in zip(names, average_grades):
    print(f"{name}: {avg:.2f}")

print(f"\nHighest Grade in Class: {highest_grade}")
print(f"Lowest Grade in Class: {lowest_grade}")
print(f"Average Grades per Subject: Math: {average_subject_grades[0]:.2f}, Science: {average_subject_grades[1]:.2f}, English: {average_subject_grades[2]:.2f}")
print(f"\nTop Performer: {top_student_name} with an average of {top_student_average:.2f}")


