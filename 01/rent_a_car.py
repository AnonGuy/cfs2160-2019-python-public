"""Apply a simple test to see if the user is old enough to rent a car."""

answer = input('Hello, who are you?\n')

while not all(word.isalpha() for word in answer.split()):
    answer = input(
        "Names usually contain letters. Let's try this again.\n"
        "Hello, who are you?\n"
    )
name = answer.title().strip()

answer = input(f'When were you born, {name}?\n')

while not answer.isnumeric():
    answer = input(
        "Years are usually numeric. Let's try this again.\n"
        f"When were you born {name}?\n"
    )
year = int(answer)

print(f'Good to meet you, {name}.')

if (age := 2019 - year) >= 21:
    print(f'{age} is old enough to rent a car.')
else:
    print(f'{age} is too young to rent a car.')
