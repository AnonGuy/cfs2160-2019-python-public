"""Output the number of labs required for a certain number of students."""

students = input('Enter the number of students: ')

while not students.isnumeric():
    students = input(
        "Numbers are usually numeric. Let's try this again.\n"
        'Enter the number of students: '
    )
students = int(students)

labs, students = divmod(students, 24)
labs += bool(students)

plural = 's' if students == 1 else ''
print(f'Lab{plural} required: {labs}')
