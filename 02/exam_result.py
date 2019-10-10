"""
Process an unlimited amount of student marks.
"""

from itertools import count


marks = []
name = input("Enter the student's name: ")

for exam in count(1):
    mark = input(f'Enter result {exam}: ')
    if mark.isnumeric():
        marks.append(int(mark))
    else:
        break

if marks:
    highest, lowest, average = (
        max(marks),
        min(marks),
        sum(marks) / len(marks)
    )
else:
    highest, lowest, average = 0, 0, 0


print(
    f'Evaluation for {name}:',
    f'Highest: {highest}',
    f'Lowest: {lowest}',
    f'Average: {average}',
    sep='\n'
)
