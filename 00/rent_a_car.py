"""Apply a simple test to see if the user is old enough to rent a car."""

name = input('Hello, who are you?\n')
answer = input(f'When were you born, {name}?\n')

while not answer.isnumeric():
    answer = input(
        "Years are usually numeric. Let's try this again.\n"
        f'How old are you, {name}?\n'
    )

year = int(answer)
age = 2019 - year

print(f'Good to meet you, {name}.')
print(f'This year you will be {age} years old.')

if age >= 21:
    print('So you can rent the car.')
else:
    print('Sorry, you are too young to rent.')
