# Lines 2 - 8 were my first attempt, blah.
# first = input('Enter the first number: ')
# second = input('Enter the second number: ')
# def multiply(): 
#    float(first) * float(second)
    
#multiply()
#print(f'{first} * {second} = ')

# Lines 11 - 16 were my second attempt, fine but could be better & no string.
# def multiply(a, b):
#    return a * b
    
# first = float(input('Enter the first number: '))
# second = float(input('Enter the frist number: '))
# print(multiply(first, second))

# Correct answer below, multiply.py
def multiply(a, b):
    return a * b
    
def get_num(prompt):
    d = input(prompt)
    return float(d)
    
first = get_num('Enter the first number: ')
second = get_num('Enter the second number: ')
answer = multiply(first, second)
print(f'{first} * {second} = {answer}')