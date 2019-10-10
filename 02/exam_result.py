"""
Process five student marks to find the average.
Display average along with the student's name.
"""

name = input("Enter the student's name: ")

marks = []
for exam in range(1, 6):
    mark = input(f'Enter result {exam}: ')
    while not mark.isnumeric():
        mark = input(
            'Marks should be numeric.\n'
            f'Enter result {exam}: '
        )
    marks.append(int(mark))

print(f'Final Mark for {name} is {sum(marks) / len(marks)}')
