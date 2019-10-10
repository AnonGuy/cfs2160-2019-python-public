"""Output the number of labs required for a certain number of students."""

students = input('Enter the number of students: ')

while not students.isnumeric():
    students = input(
        "Numbers are usually numeric. Let's try this again.\n"
        'Enter the number of students: '
    )
students = int(students)

labs, remaining = divmod(students, 24)
labs += 1 if remaining else 0

plural = 'Labs' if students == 1 else 'Lab'
print(f'{plural} required: {labs}')
