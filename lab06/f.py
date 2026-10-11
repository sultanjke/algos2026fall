def merge_sort(values):
    size = len(values)
    if size <= 1:
        return values

    middle = size // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


grades = {
    "A+": 4.00,
    "A": 3.75,
    "B+": 3.50,
    "B": 3.00,
    "C+": 2.50,
    "C": 2.00,
    "D+": 1.50,
    "D": 1.00,
    "F": 0.00
}

input = open(0).readline
n = int(input())
students = []

for student_number in range(n):
    parts = input().split()
    lastname = parts[0]
    firstname = parts[1]
    subjects = int(parts[2])
    total_points = 0.0
    total_credits = 0

    for subject in range(subjects):
        grade = parts[3 + 2 * subject]
        credits = int(parts[4 + 2 * subject])
        total_points += grades[grade] * credits
        total_credits += credits

    gpa = total_points / total_credits
    students.append((gpa, lastname, firstname))

students = merge_sort(students)
answer = []

for gpa, lastname, firstname in students:
    answer.append(f"{lastname} {firstname} {gpa:.3f}")

print("\n".join(answer))
