# age.py
age = input('How old are you? ')  # first attempt
print(f'You are {age} years old.')
print(f'In 10 years you will be {int(age) + 10} years old!')
print(f'In 20 years you will be {int(age) + 20} years old!')
print(f'In 30 years you will be {int(age) + 30} years old!')
print(f'In 40 years you will be {int(age) + 40} years old!')
print()
age = int(input('How old are you? '))  # better solution from book
print()
print(f'You are {age} years old.')
print(f'In 10 years you will be {age + 10} years old!')
print(f'In 20 years you will be {age + 20} years old!')
print(f'In 30 years you will be {age + 30} years old!')
print(f'In 40 years you will be {age + 40} years old!')