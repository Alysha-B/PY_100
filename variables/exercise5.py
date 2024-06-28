# greeter.py
name = 'Victor'
print('Good Morning, ' + name)  # first attempt, no . at the end
print('Good Morning, ' + name + '.') # worked, but long
print('Good Afternoon, ' + name + '.')
print('Good Evening, ' + name + '.')
print(f'Good Morning, {name}.')  # f-string shorter and easier
print(f'Good Afternoon, {name}.')
print(f'Good Evening, {name}.')